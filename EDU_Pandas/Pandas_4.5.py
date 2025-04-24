import pandas as pd
import matplotlib.pyplot as plt

grocery = pd.read_csv("grocery.csv")

grocery["price"].plot(
    kind = "hist",
    figsize = (10, 6),
    title = "Histogram of grocery prices",
    xticks = [2,3,4,5,6,7,8,9,10,11,12]
)

plt.savefig('output/abc.png')

grocery = grocery.sort_values(
    by="sales_date",
    ascending=True
)

grocery[grocery["product_description"]=="tomato"].plot(
    x = "sales_date", 
    y = "sales_quantity",
    kind = "line",
    figsize = (10,5),
    title = "Daily tomato sales",
    #xlabel = "Sales date",
    #ylabel = "Sales quantity"
)

plt.savefig('output/line.png')

grocery[grocery["product_description"]=="tomato"].plot(
    x = "sales_date", 
    y = ["sales_quantity", "price"],
    kind = "line",
    figsize = (10,5),
    title = "Daily tomato sales and prices",
    secondary_y = "price"
)

plt.savefig('output/secondaryline.png')