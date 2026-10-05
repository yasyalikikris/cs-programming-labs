time = 7384
hours = time//3600
minutes = (time%3600)//60
seconds = time%60
print(f'{hours:02d}:{minutes:02d}:{seconds:02d}')