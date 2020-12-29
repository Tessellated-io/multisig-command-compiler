import smartpy as sp

# This command simply transfers 1 XTZ to KT1DtPbioHJfyKxF61PxErRNkJjDyn9aDfhf
def command(self):
  transfer_operation = sp.transfer_operation(
    sp.unit,
    sp.tez(1), 
    sp.contract(None, sp.address("KT1DtPbioHJfyKxF61PxErRNkJjDyn9aDfhf")
  ).open_some())

  operation_list = [ transfer_operation ]

  sp.result(operation_list)

