


from typing import  Union
from fastapi import Body, FastAPI
from pydantic import BaseModel


app = FastAPI()
"""option_groups = {
	{
			"id": 56,
			"options": [
				{
					"id": 163,
					"is_free": True,
					"add_price": 0,
					"is_default": False,
					"list_order": 1,
					"option_code": "",
					"option_name": "pizza sosu"
				}
			],
			"max_count": 0,
			"list_order": 1,
			"description": "",
			"adding_type_id": "DECREASE",
			"choose_type_id": "MULTIPLE",
			"option_group_name": "Çıkarılacak Malzemeler"
		},
		{
			"id": 57,
			"options": [
				{
					"id": 164,
					"is_free": False,
					"add_price": 10.2,
					"is_default": True,
					"list_order": 1,
					"option_code": "",
					"option_name": "İncecik Hamur"
				},
				{
					"id": 165,
					"is_free": False,
					"add_price": 3.0,
					"is_default": False,
					"list_order": 2,
					"option_code": "",
					"option_name": "Klasik Hamur"
				}
			],
			"max_count": 0,
			"list_order": 2,
			"description": "",
			"adding_type_id": "ADD",
			"choose_type_id": "SINGLE",
			"option_group_name": "Hamur Seçimi"
		}
}

images = {
	[
		{
			"id": 804,
			"image_url": "https://siparisimcdn2.s3.eu-central-1.amazonaws.com/icdn/mobile-daily-menu-ph-margherita-big-0-6479394777655054.jpeg",
			"list_order": 1910,
			"image_size_id": "mobile_daily_menu"
		},
		{
			"id": 805,
			"image_url": "https://siparisimcdn2.s3.eu-central-1.amazonaws.com/icdn/mobile-list-ph-margherita-big-0-4629594528048909.jpeg",
			"list_order": 1910,
			"image_size_id": "mobile_list"
		},
		{
			"id": 806,
			"image_url": "https://siparisimcdn2.s3.eu-central-1.amazonaws.com/icdn/mobile-list-col-ph-margherita-big-0-9935630810104057.jpeg",
			"list_order": 1910,
			"image_size_id": "mobile_list_col"
		},
		{
			"id": 807,
			"image_url": "https://siparisimcdn2.s3.eu-central-1.amazonaws.com/icdn/mobile-detail-ph-margherita-big-0-19859779590268745.jpeg",
			"list_order": 1910,
			"image_size_id": "mobile_detail"
		}
	],
}

pprice = {
	[
		{
			"id": 110,
			"price": 37.99,
			"is_default": False,
			"order_delivery_type_id": "TABLE"
		}
	],
}"""

class Options(BaseModel):
    id:int
    is_free: Union[bool,None] = None 
    add_price: int
    is_default:bool
    list_order:int
    option_cod:Union[str,None] = None
    option_name:str

class OptionGroups(BaseModel):
    id: int
    options: Union[Options,None] = None
    max_count: int
    list_order: int
    description: Union[str,None] = None
    adding_type_id:str
    choose_typing_id:str
    options_group_name:str

class Images(BaseModel):
    id:int
    image_url: str
class Price(BaseModel):
    id:int
    price: float
    is_default: Union[bool,None] = None
    order_delivery_type_ide:str

product = {
	"id": 218,
	"product_name": "Margarita",
	"short_description": "Pizza Sosu Mozzarella Peyniri",
	"description": "",
	"product_code": "MRGT02",
	"tags": [],
	"make_time": 15,
	"calorie": 100,
	"price": [
		{
			"id": 110,
			"price": 37.99,
			"is_default": False,
			"order_delivery_type_id": "TABLE"
		}
	],
	"images": [
		{
			"id": 804,
			"image_url": "https://siparisimcdn2.s3.eu-central-1.amazonaws.com/icdn/mobile-daily-menu-ph-margherita-big-0-6479394777655054.jpeg",
			"list_order": 1910,
			"image_size_id": "mobile_daily_menu"
		},
		{
			"id": 805,
			"image_url": "https://siparisimcdn2.s3.eu-central-1.amazonaws.com/icdn/mobile-list-ph-margherita-big-0-4629594528048909.jpeg",
			"list_order": 1910,
			"image_size_id": "mobile_list"
		},
		{
			"id": 806,
			"image_url": "https://siparisimcdn2.s3.eu-central-1.amazonaws.com/icdn/mobile-list-col-ph-margherita-big-0-9935630810104057.jpeg",
			"list_order": 1910,
			"image_size_id": "mobile_list_col"
		},
		{
			"id": 807,
			"image_url": "https://siparisimcdn2.s3.eu-central-1.amazonaws.com/icdn/mobile-detail-ph-margherita-big-0-19859779590268745.jpeg",
			"list_order": 1910,
			"image_size_id": "mobile_detail"
		}
	],
	"option_groups": [
		{
			"id": 56,
			"options": [
				{
					"id": 163,
					"is_free": True,
					"add_price": 0,
					"is_default": False,
					"list_order": 1,
					"option_code": "",
					"option_name": "pizza sosu"
				}
			],
			"max_count": 0,
			"list_order": 1,
			"description": "",
			"adding_type_id": "DECREASE",
			"choose_type_id": "MULTIPLE",
			"option_group_name": "Çıkarılacak Malzemeler"
		},
		{
			"id": 57,
			"options": [
				{
					"id": 164,
					"is_free": False,
					"add_price": 10.2,
					"is_default": True,
					"list_order": 1,
					"option_code": "",
					"option_name": "İncecik Hamur"
				},
				{
					"id": 165,
					"is_free": False,
					"add_price": 3.0,
					"is_default": False,
					"list_order": 2,
					"option_code": "",
					"option_name": "Klasik Hamur"
				}
			],
			"max_count": 0,
			"list_order": 2,
			"description": "",
			"adding_type_id": "ADD",
			"choose_type_id": "SINGLE",
			"option_group_name": "Hamur Seçimi"
		}
	],
	"features": None
 }

class Product(BaseModel):
    id: int 
    product_name: str
    short_description : str
    description: Union[str,None] = None
    product_code: str
    tags : list[str] = []
    make_time: int
    calorie: int
    pricee: Union[Price,None ] = None
    images: Union[Images,None ] = None
    option_groups: Union[OptionGroups,None] = None
    features :str
    
    
@app.get("/product")
async def  read_product(product:Union[Product,None]):
    return product
    
    

@app.post("/product")
async def create_product(product: Product = Body(...,embed= True)):
    return product

@app.put("/product")
async def update_product(feature:str=Body(...,embed=True),id:int = Body(...,embed=True)):
   # a=product.get("features")
    product["features"] =feature
    product["price"][0]["id"]= id 
    
    return product
    
    
