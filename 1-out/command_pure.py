import smartpy as sp

# This command simply transfers 1 XTZ to KT1DtPbioHJfyKxF61PxErRNkJjDyn9aDfhf
def command(self):
  sp.transfer_operation(
    sp.unit,
    sp.tez(1), 
    sp.contract(None, sp.address("KT1DtPbioHJfyKxF61PxErRNkJjDyn9aDfhf")
  ).open_some())

