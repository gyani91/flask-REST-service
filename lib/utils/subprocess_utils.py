import subprocess


def executeCommand(bashCommand):
    """
    Executes a bash command as a subprocess

    :param bashCommand: the bashCommand to execute
    """
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    return process.communicate()
