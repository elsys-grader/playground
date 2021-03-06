import docker


client = docker.from_env()
labels = {'org.elsys-bg.grader': 'True'}
tag_prefix = 'elsysbg.org/grader/'

_log_config_none = {
    'type': None,
    'config': {},
}


def docker_container_prepare(docker_image, command, crippled=True,
                             volumes={},
                             **kwargs):
    kwargs['labels'] = labels
    kwargs['image'] = docker_image
    kwargs['command'] = command

    kwargs.setdefault('auto_remove', False)
    #kwargs.setdefault('log_config', _log_config_none)
    kwargs.setdefault('oom_kill_disable', False)
    kwargs.setdefault('oom_score_adj', 1000)
    kwargs.setdefault('privileged', False)
    kwargs.setdefault('stdin_open', False)
    kwargs.setdefault('tty', False)

    if crippled is True:
        kwargs.setdefault('mem_limit', '100m')
        kwargs.setdefault('mem_swappiness', 0)
        kwargs.setdefault('memswap_limit', '100m')
        kwargs.setdefault('kernel_memory', '50m')
        kwargs.setdefault('network_disabled', True)
        kwargs.setdefault('network_mode', 'none')
        kwargs.setdefault('pids_limit', 100)
        kwargs.setdefault('shm_size', '100M')
    else:
        kwargs.setdefault('network_mode', 'bridge')

    docker_volumes = {}
    for container_path, host_path in volumes.items():
        docker_volumes[host_path] = {
            'bind': container_path,
            'mode': 'ro',
        }

    kwargs['volumes'] = docker_volumes

    return kwargs


def docker_container_create(docker_image, command, **kwargs):
    kwargs = docker_container_prepare(docker_image, command, **kwargs)
    kwargs.setdefault('detach', True)
    return client.containers.create(**kwargs)


def docker_container_exec(container, command):
    exec_id = client.api.exec_create(
        container.id,
        command,
        stdout=True,
        stderr=True,
        stdin=False,
        tty=False,
        privileged=False)

    stdplex = client.api.exec_start(
        exec_id,
        detach=False,
        tty=False,
        stream=False,
        socket=False)

    exec_result = client.api.exec_inspect(exec_id)
    rc = exec_result['ExitCode']
    stdout = stderr = stdplex
    return rc, stdout, stderr, stdplex
