import matplotlib.pyplot as plt 


fig , ax =plt.subplots()

fruits=['apple','mango','banana','papaya']
counts=[13,45,6,34]
bar_labels=['red','blue','_red','orange']
bar_colors=['red','blue','red','orange']
ax.bar(fruits,counts,label=bar_labels, color=bar_colors)
plt.savefig('bars.png',bbox_inches='tight')


cats=["bored","happy","happy","happy","happy","bored"]
dogs=["happy","happy","happy","happy","bored","bored"]

activity=["combing","drinking","feeding","napping ","playing","washing"]
fig,ax=plt.subplots()
ax.plot(activity,dogs,label="dog")
ax.plot(activity,cats,label="cats")
plt.savefig('lines.png',bbox_inches='tight')