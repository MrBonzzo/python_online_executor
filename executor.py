from subprocess import Popen, PIPE, TimeoutExpired


def run(code, input_, timeout):
    preexec = ('from isolator import preparing_statements\n'
               'preparing_statements()\n')
    code_to_exec = preexec + code
    procces = Popen(['python', '-c', code_to_exec], stdin=PIPE, stdout=PIPE,
                    stderr=PIPE, encoding='utf-8')

    try:
        out, err = procces.communicate(input=input_, timeout=timeout)
    except TimeoutExpired:
        return {'out': None, 'err': None, 'timeout': True}
    return {'out': out, 'err': err, 'timeout': False}
