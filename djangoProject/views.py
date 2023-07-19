from django.shortcuts import render

def goods_view(request):
    goods_data = {
        "goods": [
            {
                "name": "Widget A",
                "size": "Small",
                "short_description": "Compact and efficient widget for everyday use."
            },
            {
                "name": "Gadget B",
                "size": "Medium",
                "short_description": "Versatile gadget with advanced features and sleek design."
            },
            {
                "name": "Device C",
                "size": "Large",
                "short_description": "Powerful device that revolutionizes the way you work and play."
            }
        ]
    }

    return render(request, 'goods.html', {"goods_data": goods_data})
