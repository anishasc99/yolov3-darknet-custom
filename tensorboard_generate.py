from torch.utils.tensorboard import SummaryWriter

writer = SummaryWriter()

 
# Using readlines()
file1 = open('tensorboard.txt', 'r')
Lines = file1.readlines()
 
count = 0
# Strips the newline character
for line in Lines:
    count += 1
    i,loss = line.strip().split(",")
    i = int(i)
    loss = float(loss)
    print(i,loss)
    writer.add_scalar("Loss/train", loss, i)
writer.flush()