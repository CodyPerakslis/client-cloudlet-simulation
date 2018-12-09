

class VirtualMachine:
    def __init__(self, provisioning_processes, cpu, memory, base_image=None):
        self.provisioning_processes = provisioning_processes
        self.cpu = cpu
        self.memory = memory
        self.base_image = base_image
