import matplotlib.pyplot as plt
import OpenPattern as OP


# Create instance of base class
p = OP.Basic_Bodice(pname = "W36G", gender = 'w', style = 'Gilewska')

# Add darts
p.add_bust_dart()
p.add_waist_dart()

# Call the draw method
p.draw({"Pattern":"Bodice with darts"},save=True)

# Look at the result
plt.show()