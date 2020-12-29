import smartpy as sp

# This command simply transfers 1 XTZ to KT1DtPbioHJfyKxF61PxErRNkJjDyn9aDfhf
def command(self, unit):
  sp.set_type(unit, sp.TUnit)

  sp.transfer_operation(
    b, 
    sp.tez(1), 
    sp.contract(None, sp.address("KT1DtPbioHJfyKxF61PxErRNkJjDyn9aDfhf")
  ).open_some())
