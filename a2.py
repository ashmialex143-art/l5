CP = int(input("enter cp of the item:"))
SP = int(input("enter sp of the item:"))

if SP > CP:
    profit=SP-CP
    print("profit: Rs.",profit)
elif SP==CP:
    print("no changes")
else:
    loss=CP-SP
    print("loss: Rs.",loss)