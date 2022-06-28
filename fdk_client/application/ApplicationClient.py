"""Application Client."""

import base64
import ujson
from urllib.parse import urlparse

from ..common.aiohttp_helper import AiohttpHelper
from ..common.exceptions import FDKClientValidationError
from ..common.utils import create_url_with_params, create_query_string, get_headers_with_signature, create_url_without_domain

from .models.CatalogValidator import CatalogValidator
from .models.CartValidator import CartValidator
from .models.CommonValidator import CommonValidator
from .models.LeadValidator import LeadValidator
from .models.ThemeValidator import ThemeValidator
from .models.UserValidator import UserValidator
from .models.ContentValidator import ContentValidator
from .models.CommunicationValidator import CommunicationValidator
from .models.ShareValidator import ShareValidator
from .models.FileStorageValidator import FileStorageValidator
from .models.ConfigurationValidator import ConfigurationValidator
from .models.PaymentValidator import PaymentValidator
from .models.OrderValidator import OrderValidator
from .models.RewardsValidator import RewardsValidator
from .models.FeedbackValidator import FeedbackValidator
from .models.PosCartValidator import PosCartValidator
from .models.LogisticValidator import LogisticValidator
from .models.LocationValidator import LocationValidator



class Catalog:
    def __init__(self, config):
        self._conf = config
        self._relativeUrls = {
            "getProductDetailBySlug": "/service/application/catalog/v1.0/products/{slug}/",
            "getProductSizesBySlug": "/service/application/catalog/v1.0/products/{slug}/sizes/",
            "getProductComparisonBySlugs": "/service/application/catalog/v1.0/products/compare/",
            "getSimilarComparisonProductBySlug": "/service/application/catalog/v1.0/products/{slug}/similar/compare/",
            "getComparedFrequentlyProductBySlug": "/service/application/catalog/v1.0/products/{slug}/similar/compared-frequently/",
            "getProductSimilarByIdentifier": "/service/application/catalog/v1.0/products/{slug}/similar/{similar_type}/",
            "getProductVariantsBySlug": "/service/application/catalog/v1.0/products/{slug}/variants/",
            "getProductStockByIds": "/service/application/catalog/v1.0/products/stock-status/",
            "getProductStockForTimeByIds": "/service/application/catalog/v1.0/products/stock-status/poll/",
            "getProducts": "/service/application/catalog/v1.0/products/",
            "getBrands": "/service/application/catalog/v1.0/brands/",
            "getBrandDetailBySlug": "/service/application/catalog/v1.0/brands/{slug}/",
            "getCategories": "/service/application/catalog/v1.0/categories/",
            "getCategoryDetailBySlug": "/service/application/catalog/v1.0/categories/{slug}/",
            "getHomeProducts": "/service/application/catalog/v1.0/home/listing/",
            "getDepartments": "/service/application/catalog/v1.0/departments/",
            "getSearchResults": "/service/application/catalog/v1.0/auto-complete/",
            "getCollections": "/service/application/catalog/v1.0/collections/",
            "getCollectionItemsBySlug": "/service/application/catalog/v1.0/collections/{slug}/items/",
            "getCollectionDetailBySlug": "/service/application/catalog/v1.0/collections/{slug}/",
            "getFollowedListing": "/service/application/catalog/v1.0/follow/{collection_type}/",
            "unfollowById": "/service/application/catalog/v1.0/follow/{collection_type}/{collection_id}/",
            "followById": "/service/application/catalog/v1.0/follow/{collection_type}/{collection_id}/",
            "getFollowerCountById": "/service/application/catalog/v1.0/follow/{collection_type}/{collection_id}/count/",
            "getFollowIds": "/service/application/catalog/v1.0/follow/ids/",
            "getStores": "/service/application/catalog/v1.0/locations/",
            "getInStockLocations": "/service/application/catalog/v1.0/in-stock/locations/",
            "getLocationDetailsById": "/service/application/catalog/v1.0/locations/{location_id}/",
            "getProductBundlesBySlug": "/service/application/catalog/v1.0/product-grouping/",
            "getProductPriceBySlug": "/service/application/catalog/v2.0/products/{slug}/sizes/{size}/price/",
            "getProductSellersBySlug": "/service/application/catalog/v2.0/products/{slug}/sizes/{size}/sellers/"
            
        }
        self._urls = {
            method: f"{self._conf.domain}{path}" for method, path in self._relativeUrls.items()
        }

    async def updateUrls(self, urls):
        self._urls.update(urls)
    
    async def getProductDetailBySlug(self, slug=None, body=""):
        """Use this API to retrieve a product by its slug value.
        :param slug : A short, human-readable, URL-friendly identifier of a product. You can get slug value from the endpoint /service/application/catalog/v1.0/products/ : type string
        """
        payload = {}
        
        if slug:
            payload["slug"] = slug
        
        # Parameter validation
        schema = CatalogValidator.getProductDetailBySlug()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getProductDetailBySlug"], proccessed_params="""{"required":[{"in":"path","name":"slug","description":"A short, human-readable, URL-friendly identifier of a product. You can get slug value from the endpoint /service/application/catalog/v1.0/products/","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"slug","description":"A short, human-readable, URL-friendly identifier of a product. You can get slug value from the endpoint /service/application/catalog/v1.0/products/","schema":{"type":"string"},"required":true}]}""", slug=slug)
        query_string = await create_query_string(slug=slug)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getProductDetailBySlug"]).netloc, "get", await create_url_without_domain("/service/application/catalog/v1.0/products/{slug}/", slug=slug), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getProductSizesBySlug(self, slug=None, store_id=None, body=""):
        """A product can have multiple sizes. Use this API to fetch all the available sizes of a product.
        :param slug : A short, human-readable, URL-friendly identifier of a product. You can get slug value from the endpoint /service/application/catalog/v1.0/products/ : type string
        :param store_id : The ID of the store that is selling the product, e.g. 1,2,3. : type integer
        """
        payload = {}
        
        if slug:
            payload["slug"] = slug
        
        if store_id:
            payload["store_id"] = store_id
        
        # Parameter validation
        schema = CatalogValidator.getProductSizesBySlug()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getProductSizesBySlug"], proccessed_params="""{"required":[{"in":"path","name":"slug","description":"A short, human-readable, URL-friendly identifier of a product. You can get slug value from the endpoint /service/application/catalog/v1.0/products/","schema":{"type":"string"},"required":true}],"optional":[{"in":"query","name":"store_id","description":"The ID of the store that is selling the product, e.g. 1,2,3.","schema":{"type":"integer"},"required":false}],"query":[{"in":"query","name":"store_id","description":"The ID of the store that is selling the product, e.g. 1,2,3.","schema":{"type":"integer"},"required":false}],"headers":[],"path":[{"in":"path","name":"slug","description":"A short, human-readable, URL-friendly identifier of a product. You can get slug value from the endpoint /service/application/catalog/v1.0/products/","schema":{"type":"string"},"required":true}]}""", slug=slug, store_id=store_id)
        query_string = await create_query_string(slug=slug, store_id=store_id)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getProductSizesBySlug"]).netloc, "get", await create_url_without_domain("/service/application/catalog/v1.0/products/{slug}/sizes/", slug=slug, store_id=store_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getProductComparisonBySlugs(self, slug=None, body=""):
        """Use this API to compare the features of products belonging to the same category. Note that at least one slug is mandatory in the request query.
        :param slug : A short, human-readable, URL-friendly identifier of a product. You can get slug value from the endpoint /service/application/catalog/v1.0/products/. : type array
        """
        payload = {}
        
        if slug:
            payload["slug"] = slug
        
        # Parameter validation
        schema = CatalogValidator.getProductComparisonBySlugs()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getProductComparisonBySlugs"], proccessed_params="""{"required":[{"in":"query","name":"slug","description":"A short, human-readable, URL-friendly identifier of a product. You can get slug value from the endpoint /service/application/catalog/v1.0/products/.","schema":{"type":"array","items":{"type":"string"},"minItems":1},"required":true}],"optional":[],"query":[{"in":"query","name":"slug","description":"A short, human-readable, URL-friendly identifier of a product. You can get slug value from the endpoint /service/application/catalog/v1.0/products/.","schema":{"type":"array","items":{"type":"string"},"minItems":1},"required":true}],"headers":[],"path":[]}""", slug=slug)
        query_string = await create_query_string(slug=slug)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getProductComparisonBySlugs"]).netloc, "get", await create_url_without_domain("/service/application/catalog/v1.0/products/compare/", slug=slug), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getSimilarComparisonProductBySlug(self, slug=None, body=""):
        """Use this API to compare a given product automatically with similar products. Only one slug is needed.
        :param slug : A short, human-readable, URL-friendly identifier of a product. You can get slug value from the endpoint /service/application/catalog/v1.0/products/ : type string
        """
        payload = {}
        
        if slug:
            payload["slug"] = slug
        
        # Parameter validation
        schema = CatalogValidator.getSimilarComparisonProductBySlug()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getSimilarComparisonProductBySlug"], proccessed_params="""{"required":[{"in":"path","name":"slug","description":"A short, human-readable, URL-friendly identifier of a product. You can get slug value from the endpoint /service/application/catalog/v1.0/products/","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"slug","description":"A short, human-readable, URL-friendly identifier of a product. You can get slug value from the endpoint /service/application/catalog/v1.0/products/","schema":{"type":"string"},"required":true}]}""", slug=slug)
        query_string = await create_query_string(slug=slug)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getSimilarComparisonProductBySlug"]).netloc, "get", await create_url_without_domain("/service/application/catalog/v1.0/products/{slug}/similar/compare/", slug=slug), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getComparedFrequentlyProductBySlug(self, slug=None, body=""):
        """Use this API to compare a given product automatically with products that are frequently compared with it. Only one slug is needed.
        :param slug : A short, human-readable, URL-friendly identifier of a product. You can get slug value from the endpoint /service/application/catalog/v1.0/products/ : type string
        """
        payload = {}
        
        if slug:
            payload["slug"] = slug
        
        # Parameter validation
        schema = CatalogValidator.getComparedFrequentlyProductBySlug()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getComparedFrequentlyProductBySlug"], proccessed_params="""{"required":[{"in":"path","name":"slug","description":"A short, human-readable, URL-friendly identifier of a product. You can get slug value from the endpoint /service/application/catalog/v1.0/products/","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"slug","description":"A short, human-readable, URL-friendly identifier of a product. You can get slug value from the endpoint /service/application/catalog/v1.0/products/","schema":{"type":"string"},"required":true}]}""", slug=slug)
        query_string = await create_query_string(slug=slug)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getComparedFrequentlyProductBySlug"]).netloc, "get", await create_url_without_domain("/service/application/catalog/v1.0/products/{slug}/similar/compared-frequently/", slug=slug), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getProductSimilarByIdentifier(self, slug=None, similar_type=None, body=""):
        """Use this API to retrieve products similar to the one specified by its slug. You can search not only similar looking products, but also those that are sold by same seller, or those that belong to the same category, price, specifications, etc.
        :param slug : A short, human-readable, URL-friendly identifier of a product. You can get slug value from the endpoint /service/application/catalog/v1.0/products/ : type string
        :param similar_type : Similarity criteria such as basic, visual, price, seller, category and spec. Visual - Products having similar patterns, Price - Products in similar price range, Seller - Products sold by the same seller, Category - Products belonging to the same category, e.g. sports shoes, Spec - Products having similar specifications, e.g. phones with same memory. : type string
        """
        payload = {}
        
        if slug:
            payload["slug"] = slug
        
        if similar_type:
            payload["similar_type"] = similar_type
        
        # Parameter validation
        schema = CatalogValidator.getProductSimilarByIdentifier()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getProductSimilarByIdentifier"], proccessed_params="""{"required":[{"in":"path","name":"slug","description":"A short, human-readable, URL-friendly identifier of a product. You can get slug value from the endpoint /service/application/catalog/v1.0/products/","schema":{"type":"string"},"required":true},{"in":"path","name":"similar_type","description":"Similarity criteria such as basic, visual, price, seller, category and spec. Visual - Products having similar patterns, Price - Products in similar price range, Seller - Products sold by the same seller, Category - Products belonging to the same category, e.g. sports shoes, Spec - Products having similar specifications, e.g. phones with same memory.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"slug","description":"A short, human-readable, URL-friendly identifier of a product. You can get slug value from the endpoint /service/application/catalog/v1.0/products/","schema":{"type":"string"},"required":true},{"in":"path","name":"similar_type","description":"Similarity criteria such as basic, visual, price, seller, category and spec. Visual - Products having similar patterns, Price - Products in similar price range, Seller - Products sold by the same seller, Category - Products belonging to the same category, e.g. sports shoes, Spec - Products having similar specifications, e.g. phones with same memory.","schema":{"type":"string"},"required":true}]}""", slug=slug, similar_type=similar_type)
        query_string = await create_query_string(slug=slug, similar_type=similar_type)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getProductSimilarByIdentifier"]).netloc, "get", await create_url_without_domain("/service/application/catalog/v1.0/products/{slug}/similar/{similar_type}/", slug=slug, similar_type=similar_type), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getProductVariantsBySlug(self, slug=None, body=""):
        """A product can have a different type of variants such as colour, shade, memory. Use this API to fetch all the available variants of a product using its slug.
        :param slug : A short, human-readable, URL-friendly identifier of a product. You can get slug value from the endpoint /service/application/catalog/v1.0/products/ : type string
        """
        payload = {}
        
        if slug:
            payload["slug"] = slug
        
        # Parameter validation
        schema = CatalogValidator.getProductVariantsBySlug()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getProductVariantsBySlug"], proccessed_params="""{"required":[{"in":"path","name":"slug","description":"A short, human-readable, URL-friendly identifier of a product. You can get slug value from the endpoint /service/application/catalog/v1.0/products/","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"slug","description":"A short, human-readable, URL-friendly identifier of a product. You can get slug value from the endpoint /service/application/catalog/v1.0/products/","schema":{"type":"string"},"required":true}]}""", slug=slug)
        query_string = await create_query_string(slug=slug)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getProductVariantsBySlug"]).netloc, "get", await create_url_without_domain("/service/application/catalog/v1.0/products/{slug}/variants/", slug=slug), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getProductStockByIds(self, item_id=None, alu=None, sku_code=None, ean=None, upc=None, body=""):
        """Retrieve the available stock of the products. Use this API to retrieve stock of multiple products (up to 50) at a time.
        :param item_id : The Item ID of the product (Max. 50 allowed) : type string
        :param alu : ALU of the product (limited upto 50 ALU identifier in a single request) : type string
        :param sku_code : Stock-keeping Unit of the product (limited upto 50 SKU Code in a single request) : type string
        :param ean : European Article Number of the product (limited upto 50 EAN identifier in a single request) : type string
        :param upc : Universal Product Code of the product (limited upto 50 UPC identifier in a single request) : type string
        """
        payload = {}
        
        if item_id:
            payload["item_id"] = item_id
        
        if alu:
            payload["alu"] = alu
        
        if sku_code:
            payload["sku_code"] = sku_code
        
        if ean:
            payload["ean"] = ean
        
        if upc:
            payload["upc"] = upc
        
        # Parameter validation
        schema = CatalogValidator.getProductStockByIds()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getProductStockByIds"], proccessed_params="""{"required":[],"optional":[{"in":"query","name":"item_id","description":"The Item ID of the product (Max. 50 allowed)","schema":{"type":"string"},"required":false},{"in":"query","name":"alu","description":"ALU of the product (limited upto 50 ALU identifier in a single request)","schema":{"type":"string"},"required":false},{"in":"query","name":"sku_code","description":"Stock-keeping Unit of the product (limited upto 50 SKU Code in a single request)","schema":{"type":"string"},"required":false},{"in":"query","name":"ean","description":"European Article Number of the product (limited upto 50 EAN identifier in a single request)","schema":{"type":"string"},"required":false},{"in":"query","name":"upc","description":"Universal Product Code of the product (limited upto 50 UPC identifier in a single request)","schema":{"type":"string"},"required":false}],"query":[{"in":"query","name":"item_id","description":"The Item ID of the product (Max. 50 allowed)","schema":{"type":"string"},"required":false},{"in":"query","name":"alu","description":"ALU of the product (limited upto 50 ALU identifier in a single request)","schema":{"type":"string"},"required":false},{"in":"query","name":"sku_code","description":"Stock-keeping Unit of the product (limited upto 50 SKU Code in a single request)","schema":{"type":"string"},"required":false},{"in":"query","name":"ean","description":"European Article Number of the product (limited upto 50 EAN identifier in a single request)","schema":{"type":"string"},"required":false},{"in":"query","name":"upc","description":"Universal Product Code of the product (limited upto 50 UPC identifier in a single request)","schema":{"type":"string"},"required":false}],"headers":[],"path":[]}""", item_id=item_id, alu=alu, sku_code=sku_code, ean=ean, upc=upc)
        query_string = await create_query_string(item_id=item_id, alu=alu, sku_code=sku_code, ean=ean, upc=upc)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getProductStockByIds"]).netloc, "get", await create_url_without_domain("/service/application/catalog/v1.0/products/stock-status/", item_id=item_id, alu=alu, sku_code=sku_code, ean=ean, upc=upc), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getProductStockForTimeByIds(self, timestamp=None, page_size=None, page_id=None, body=""):
        """Retrieve the available stock of the products. Use this API to get the stock status of products whose inventory is updated at the specified time
        :param timestamp : Timestamp in UTC format (2020-07-23T10:27:50Z) : type string
        :param page_size : The number of items to retrieve in each page. : type integer
        :param page_id : Page ID to retrieve next set of results. : type string
        """
        payload = {}
        
        if timestamp:
            payload["timestamp"] = timestamp
        
        if page_size:
            payload["page_size"] = page_size
        
        if page_id:
            payload["page_id"] = page_id
        
        # Parameter validation
        schema = CatalogValidator.getProductStockForTimeByIds()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getProductStockForTimeByIds"], proccessed_params="""{"required":[{"in":"query","name":"timestamp","description":"Timestamp in UTC format (2020-07-23T10:27:50Z)","schema":{"type":"string"},"required":true}],"optional":[{"in":"query","name":"page_size","description":"The number of items to retrieve in each page.","schema":{"type":"integer","default":12},"required":false},{"in":"query","name":"page_id","description":"Page ID to retrieve next set of results.","schema":{"type":"string"},"required":false}],"query":[{"in":"query","name":"timestamp","description":"Timestamp in UTC format (2020-07-23T10:27:50Z)","schema":{"type":"string"},"required":true},{"in":"query","name":"page_size","description":"The number of items to retrieve in each page.","schema":{"type":"integer","default":12},"required":false},{"in":"query","name":"page_id","description":"Page ID to retrieve next set of results.","schema":{"type":"string"},"required":false}],"headers":[],"path":[]}""", timestamp=timestamp, page_size=page_size, page_id=page_id)
        query_string = await create_query_string(timestamp=timestamp, page_size=page_size, page_id=page_id)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getProductStockForTimeByIds"]).netloc, "get", await create_url_without_domain("/service/application/catalog/v1.0/products/stock-status/poll/", timestamp=timestamp, page_size=page_size, page_id=page_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getProducts(self, q=None, f=None, filters=None, sort_on=None, page_id=None, page_size=None, page_no=None, page_type=None, body=""):
        """Use this API to list all the products. You may choose a sort order or make arbitrary search queries by entering the product name, brand, category or collection.
        :param q : The search query for entering partial or full name of product, brand, category, or collection. : type string
        :param f : The search filter parameters. Filter parameters will be passed in f parameter as shown in the example below. Double Pipe (||) denotes the OR condition, whereas Triple-colon (:::) indicates a new filter paramater applied as an AND condition. : type string
        :param filters : This is a boolean value, True for fetching all filter parameters and False for disabling the filter parameters. : type boolean
        :param sort_on : The order in which the list of products should be sorted, e.g. popularity, price, latest and discount, in either ascending or descending order. See the supported values below. : type string
        :param page_id : Page ID to retrieve next set of results. : type string
        :param page_size : The number of items to retrieve in each page. : type integer
        :param page_no : The page number to navigate through the given set of results. : type integer
        :param page_type : Available pagination types are cursor or number. : type string
        """
        payload = {}
        
        if q:
            payload["q"] = q
        
        if f:
            payload["f"] = f
        
        if filters:
            payload["filters"] = filters
        
        if sort_on:
            payload["sort_on"] = sort_on
        
        if page_id:
            payload["page_id"] = page_id
        
        if page_size:
            payload["page_size"] = page_size
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_type:
            payload["page_type"] = page_type
        
        # Parameter validation
        schema = CatalogValidator.getProducts()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getProducts"], proccessed_params="""{"required":[],"optional":[{"in":"query","name":"q","description":"The search query for entering partial or full name of product, brand, category, or collection.","schema":{"type":"string"},"required":false},{"in":"query","name":"f","description":"The search filter parameters. Filter parameters will be passed in f parameter as shown in the example below. Double Pipe (||) denotes the OR condition, whereas Triple-colon (:::) indicates a new filter paramater applied as an AND condition.","schema":{"type":"string","example":"brand:voi-jeans||reliance:::l3_categories:t-shirts||shirts"},"required":false},{"in":"query","name":"filters","description":"This is a boolean value, True for fetching all filter parameters and False for disabling the filter parameters.","schema":{"type":"boolean","default":true},"required":false},{"in":"query","name":"sort_on","description":"The order in which the list of products should be sorted, e.g. popularity, price, latest and discount, in either ascending or descending order. See the supported values below.","schema":{"type":"string","enum":["latest","popular","price_asc","price_dsc","discount_asc","discount_dsc"]},"required":false},{"in":"query","name":"page_id","description":"Page ID to retrieve next set of results.","schema":{"type":"string"},"required":false},{"in":"query","name":"page_size","description":"The number of items to retrieve in each page.","schema":{"type":"integer","default":12},"required":false},{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results.","schema":{"type":"integer","default":1},"required":false},{"in":"query","name":"page_type","description":"Available pagination types are cursor or number.","schema":{"type":"string","default":"cursor"},"required":false}],"query":[{"in":"query","name":"q","description":"The search query for entering partial or full name of product, brand, category, or collection.","schema":{"type":"string"},"required":false},{"in":"query","name":"f","description":"The search filter parameters. Filter parameters will be passed in f parameter as shown in the example below. Double Pipe (||) denotes the OR condition, whereas Triple-colon (:::) indicates a new filter paramater applied as an AND condition.","schema":{"type":"string","example":"brand:voi-jeans||reliance:::l3_categories:t-shirts||shirts"},"required":false},{"in":"query","name":"filters","description":"This is a boolean value, True for fetching all filter parameters and False for disabling the filter parameters.","schema":{"type":"boolean","default":true},"required":false},{"in":"query","name":"sort_on","description":"The order in which the list of products should be sorted, e.g. popularity, price, latest and discount, in either ascending or descending order. See the supported values below.","schema":{"type":"string","enum":["latest","popular","price_asc","price_dsc","discount_asc","discount_dsc"]},"required":false},{"in":"query","name":"page_id","description":"Page ID to retrieve next set of results.","schema":{"type":"string"},"required":false},{"in":"query","name":"page_size","description":"The number of items to retrieve in each page.","schema":{"type":"integer","default":12},"required":false},{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results.","schema":{"type":"integer","default":1},"required":false},{"in":"query","name":"page_type","description":"Available pagination types are cursor or number.","schema":{"type":"string","default":"cursor"},"required":false}],"headers":[],"path":[]}""", q=q, f=f, filters=filters, sort_on=sort_on, page_id=page_id, page_size=page_size, page_no=page_no, page_type=page_type)
        query_string = await create_query_string(q=q, f=f, filters=filters, sort_on=sort_on, page_id=page_id, page_size=page_size, page_no=page_no, page_type=page_type)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getProducts"]).netloc, "get", await create_url_without_domain("/service/application/catalog/v1.0/products/", q=q, f=f, filters=filters, sort_on=sort_on, page_id=page_id, page_size=page_size, page_no=page_no, page_type=page_type), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getBrands(self, department=None, page_no=None, page_size=None, body=""):
        """A brand is the name under which a product is sold. Use this API to list all the brands. You can also filter the brands by department.
        :param department : The name of the department. Use this parameter to filter products by a particular department. See the list of available departments below. Also, you can get available departments from the endpoint /service/application/catalog/v1.0/departments/ : type string
        :param page_no : The page number to navigate through the given set of results. : type integer
        :param page_size : The number of items to retrieve in each page. : type integer
        """
        payload = {}
        
        if department:
            payload["department"] = department
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        
        # Parameter validation
        schema = CatalogValidator.getBrands()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getBrands"], proccessed_params="""{"required":[],"optional":[{"in":"query","name":"department","description":"The name of the department. Use this parameter to filter products by a particular department. See the list of available departments below. Also, you can get available departments from the endpoint /service/application/catalog/v1.0/departments/","schema":{"type":"string","enum":["baby-care-kids-essentials","beauty-personal-care","home-living","fashion","others","toys"]},"required":false},{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results.","schema":{"type":"integer","default":1},"required":false},{"in":"query","name":"page_size","description":"The number of items to retrieve in each page.","schema":{"type":"integer","default":12},"required":false}],"query":[{"in":"query","name":"department","description":"The name of the department. Use this parameter to filter products by a particular department. See the list of available departments below. Also, you can get available departments from the endpoint /service/application/catalog/v1.0/departments/","schema":{"type":"string","enum":["baby-care-kids-essentials","beauty-personal-care","home-living","fashion","others","toys"]},"required":false},{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results.","schema":{"type":"integer","default":1},"required":false},{"in":"query","name":"page_size","description":"The number of items to retrieve in each page.","schema":{"type":"integer","default":12},"required":false}],"headers":[],"path":[]}""", department=department, page_no=page_no, page_size=page_size)
        query_string = await create_query_string(department=department, page_no=page_no, page_size=page_size)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getBrands"]).netloc, "get", await create_url_without_domain("/service/application/catalog/v1.0/brands/", department=department, page_no=page_no, page_size=page_size), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getBrandDetailBySlug(self, slug=None, body=""):
        """Fetch metadata of a brand such as name, information, logo, banner, etc.
        :param slug : A short, human-readable, URL-friendly identifier of a brand. You can get slug value from the endpoint /service/application/catalog/v1.0/brands/. : type string
        """
        payload = {}
        
        if slug:
            payload["slug"] = slug
        
        # Parameter validation
        schema = CatalogValidator.getBrandDetailBySlug()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getBrandDetailBySlug"], proccessed_params="""{"required":[{"in":"path","name":"slug","description":"A short, human-readable, URL-friendly identifier of a brand. You can get slug value from the endpoint /service/application/catalog/v1.0/brands/.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"slug","description":"A short, human-readable, URL-friendly identifier of a brand. You can get slug value from the endpoint /service/application/catalog/v1.0/brands/.","schema":{"type":"string"},"required":true}]}""", slug=slug)
        query_string = await create_query_string(slug=slug)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getBrandDetailBySlug"]).netloc, "get", await create_url_without_domain("/service/application/catalog/v1.0/brands/{slug}/", slug=slug), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getCategories(self, department=None, body=""):
        """Use this API to list all the categories. You can also filter the categories by department.
        :param department : The name of the department. Use this parameter to filter products by a particular department. See the list of available departments below. Also, you can get available departments from the endpoint /service/application/catalog/v1.0/departments/ : type string
        """
        payload = {}
        
        if department:
            payload["department"] = department
        
        # Parameter validation
        schema = CatalogValidator.getCategories()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getCategories"], proccessed_params="""{"required":[],"optional":[{"in":"query","name":"department","description":"The name of the department. Use this parameter to filter products by a particular department. See the list of available departments below. Also, you can get available departments from the endpoint /service/application/catalog/v1.0/departments/","schema":{"type":"string","enum":["baby-care-kids-essentials","beauty-personal-care","home-living","fashion","others","toys"]},"required":false}],"query":[{"in":"query","name":"department","description":"The name of the department. Use this parameter to filter products by a particular department. See the list of available departments below. Also, you can get available departments from the endpoint /service/application/catalog/v1.0/departments/","schema":{"type":"string","enum":["baby-care-kids-essentials","beauty-personal-care","home-living","fashion","others","toys"]},"required":false}],"headers":[],"path":[]}""", department=department)
        query_string = await create_query_string(department=department)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getCategories"]).netloc, "get", await create_url_without_domain("/service/application/catalog/v1.0/categories/", department=department), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getCategoryDetailBySlug(self, slug=None, body=""):
        """Fetch metadata of a category such as name, information, logo, banner, etc.
        :param slug : A short, human-readable, URL-friendly identifier of a brand. You can get slug value from the endpoint /service/application/catalog/v1.0/brands/. : type string
        """
        payload = {}
        
        if slug:
            payload["slug"] = slug
        
        # Parameter validation
        schema = CatalogValidator.getCategoryDetailBySlug()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getCategoryDetailBySlug"], proccessed_params="""{"required":[{"in":"path","name":"slug","description":"A short, human-readable, URL-friendly identifier of a brand. You can get slug value from the endpoint /service/application/catalog/v1.0/brands/.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"slug","description":"A short, human-readable, URL-friendly identifier of a brand. You can get slug value from the endpoint /service/application/catalog/v1.0/brands/.","schema":{"type":"string"},"required":true}]}""", slug=slug)
        query_string = await create_query_string(slug=slug)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getCategoryDetailBySlug"]).netloc, "get", await create_url_without_domain("/service/application/catalog/v1.0/categories/{slug}/", slug=slug), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getHomeProducts(self, sort_on=None, page_id=None, page_size=None, body=""):
        """List all the products associated with a brand, collection or category in a random order.
        :param sort_on : The order in which the list of products should be sorted, e.g. popularity, price, latest and discount, in either ascending or descending order. : type string
        :param page_id : Page ID to retrieve next set of results. : type string
        :param page_size : The number of items to retrieve in each page. : type integer
        """
        payload = {}
        
        if sort_on:
            payload["sort_on"] = sort_on
        
        if page_id:
            payload["page_id"] = page_id
        
        if page_size:
            payload["page_size"] = page_size
        
        # Parameter validation
        schema = CatalogValidator.getHomeProducts()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getHomeProducts"], proccessed_params="""{"required":[],"optional":[{"in":"query","name":"sort_on","description":"The order in which the list of products should be sorted, e.g. popularity, price, latest and discount, in either ascending or descending order.","schema":{"type":"string"},"required":false},{"in":"query","name":"page_id","description":"Page ID to retrieve next set of results.","schema":{"type":"string","default":1},"required":false},{"in":"query","name":"page_size","description":"The number of items to retrieve in each page.","schema":{"type":"integer","default":12},"required":false}],"query":[{"in":"query","name":"sort_on","description":"The order in which the list of products should be sorted, e.g. popularity, price, latest and discount, in either ascending or descending order.","schema":{"type":"string"},"required":false},{"in":"query","name":"page_id","description":"Page ID to retrieve next set of results.","schema":{"type":"string","default":1},"required":false},{"in":"query","name":"page_size","description":"The number of items to retrieve in each page.","schema":{"type":"integer","default":12},"required":false}],"headers":[],"path":[]}""", sort_on=sort_on, page_id=page_id, page_size=page_size)
        query_string = await create_query_string(sort_on=sort_on, page_id=page_id, page_size=page_size)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getHomeProducts"]).netloc, "get", await create_url_without_domain("/service/application/catalog/v1.0/home/listing/", sort_on=sort_on, page_id=page_id, page_size=page_size), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getDepartments(self, body=""):
        """Departments are a way to categorise similar products. A product can lie in multiple departments. For example, a skirt can below to the 'Women's Fashion' Department while a handbag can lie in 'Women's Accessories' Department. Use this API to list all the departments. If successful, returns the list of departments specified in `DepartmentResponse`
        """
        payload = {}
        
        # Parameter validation
        schema = CatalogValidator.getDepartments()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getDepartments"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getDepartments"]).netloc, "get", await create_url_without_domain("/service/application/catalog/v1.0/departments/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getSearchResults(self, q=None, body=""):
        """Retrieves a list of suggestions for a given search query. Each suggestion is a valid search term that's generated on the basis of query. This is particularly useful to enhance the user experience while using the search tool.
        :param q : The search query for entering partial or full name of a product, brand or category. For example, if the given search query `q` is _ski_, the relevant search suggestions could be _skirt_, _ski shoes_, __skin cream_ etc. : type string
        """
        payload = {}
        
        if q:
            payload["q"] = q
        
        # Parameter validation
        schema = CatalogValidator.getSearchResults()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getSearchResults"], proccessed_params="""{"required":[{"in":"query","name":"q","description":"The search query for entering partial or full name of a product, brand or category. For example, if the given search query `q` is _ski_, the relevant search suggestions could be _skirt_, _ski shoes_, __skin cream_ etc.","schema":{"type":"string"},"required":true}],"optional":[],"query":[{"in":"query","name":"q","description":"The search query for entering partial or full name of a product, brand or category. For example, if the given search query `q` is _ski_, the relevant search suggestions could be _skirt_, _ski shoes_, __skin cream_ etc.","schema":{"type":"string"},"required":true}],"headers":[],"path":[]}""", q=q)
        query_string = await create_query_string(q=q)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getSearchResults"]).netloc, "get", await create_url_without_domain("/service/application/catalog/v1.0/auto-complete/", q=q), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getCollections(self, page_no=None, page_size=None, tag=None, body=""):
        """Collections are a great way to organize your products and can improve the ability for customers to find items quickly and efficiently.
        :param page_no : The page number to navigate through the given set of results. : type integer
        :param page_size : The number of items to retrieve in each page. : type integer
        :param tag : List of tags  to filter collections : type array
        """
        payload = {}
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        
        if tag:
            payload["tag"] = tag
        
        # Parameter validation
        schema = CatalogValidator.getCollections()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getCollections"], proccessed_params="""{"required":[],"optional":[{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results.","schema":{"type":"integer","default":1},"required":false},{"in":"query","name":"page_size","description":"The number of items to retrieve in each page.","schema":{"type":"integer","default":12},"required":false},{"in":"query","name":"tag","description":"List of tags  to filter collections","schema":{"type":"array","items":{"type":"string"},"minItems":1},"required":false}],"query":[{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results.","schema":{"type":"integer","default":1},"required":false},{"in":"query","name":"page_size","description":"The number of items to retrieve in each page.","schema":{"type":"integer","default":12},"required":false},{"in":"query","name":"tag","description":"List of tags  to filter collections","schema":{"type":"array","items":{"type":"string"},"minItems":1},"required":false}],"headers":[],"path":[]}""", page_no=page_no, page_size=page_size, tag=tag)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, tag=tag)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getCollections"]).netloc, "get", await create_url_without_domain("/service/application/catalog/v1.0/collections/", page_no=page_no, page_size=page_size, tag=tag), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getCollectionItemsBySlug(self, slug=None, f=None, filters=None, sort_on=None, page_id=None, page_size=None, body=""):
        """Get items in a collection specified by its `slug`.
        :param slug : A short, human-readable, URL-friendly identifier of a collection. You can get slug value from the endpoint /service/application/catalog/v1.0/collections/. : type string
        :param f : The search filter parameters. Filter parameters will be passed in f parameter as shown in the example below. Double Pipe (||) denotes the OR condition, whereas Triple-colon (:::) indicates a new filter paramater applied as an AND condition. : type string
        :param filters : This is a boolean value, True for fetching all filter parameters and False for disabling the filter parameters. : type boolean
        :param sort_on : The order in which the list of products should be sorted, e.g. popularity, price, latest and discount, in either ascending or descending order. See the supported values below. : type string
        :param page_id : Page ID to retrieve next set of results. : type string
        :param page_size : The number of items to retrieve in each page. : type integer
        """
        payload = {}
        
        if slug:
            payload["slug"] = slug
        
        if f:
            payload["f"] = f
        
        if filters:
            payload["filters"] = filters
        
        if sort_on:
            payload["sort_on"] = sort_on
        
        if page_id:
            payload["page_id"] = page_id
        
        if page_size:
            payload["page_size"] = page_size
        
        # Parameter validation
        schema = CatalogValidator.getCollectionItemsBySlug()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getCollectionItemsBySlug"], proccessed_params="""{"required":[{"in":"path","name":"slug","description":"A short, human-readable, URL-friendly identifier of a collection. You can get slug value from the endpoint /service/application/catalog/v1.0/collections/.","schema":{"type":"string"},"required":true}],"optional":[{"in":"query","name":"f","description":"The search filter parameters. Filter parameters will be passed in f parameter as shown in the example below. Double Pipe (||) denotes the OR condition, whereas Triple-colon (:::) indicates a new filter paramater applied as an AND condition.","schema":{"type":"string","example":"brand:voi-jeans||reliance:::l3_categories:t-shirts||shirts"},"required":false},{"in":"query","name":"filters","description":"This is a boolean value, True for fetching all filter parameters and False for disabling the filter parameters.","schema":{"type":"boolean","default":true},"required":false},{"in":"query","name":"sort_on","description":"The order in which the list of products should be sorted, e.g. popularity, price, latest and discount, in either ascending or descending order. See the supported values below.","schema":{"type":"string","enum":["latest","popular","price_asc","price_dsc","discount_asc","discount_dsc"]},"required":false},{"in":"query","name":"page_id","description":"Page ID to retrieve next set of results.","schema":{"type":"string","default":1},"required":false},{"in":"query","name":"page_size","description":"The number of items to retrieve in each page.","schema":{"type":"integer","default":12},"required":false}],"query":[{"in":"query","name":"f","description":"The search filter parameters. Filter parameters will be passed in f parameter as shown in the example below. Double Pipe (||) denotes the OR condition, whereas Triple-colon (:::) indicates a new filter paramater applied as an AND condition.","schema":{"type":"string","example":"brand:voi-jeans||reliance:::l3_categories:t-shirts||shirts"},"required":false},{"in":"query","name":"filters","description":"This is a boolean value, True for fetching all filter parameters and False for disabling the filter parameters.","schema":{"type":"boolean","default":true},"required":false},{"in":"query","name":"sort_on","description":"The order in which the list of products should be sorted, e.g. popularity, price, latest and discount, in either ascending or descending order. See the supported values below.","schema":{"type":"string","enum":["latest","popular","price_asc","price_dsc","discount_asc","discount_dsc"]},"required":false},{"in":"query","name":"page_id","description":"Page ID to retrieve next set of results.","schema":{"type":"string","default":1},"required":false},{"in":"query","name":"page_size","description":"The number of items to retrieve in each page.","schema":{"type":"integer","default":12},"required":false}],"headers":[],"path":[{"in":"path","name":"slug","description":"A short, human-readable, URL-friendly identifier of a collection. You can get slug value from the endpoint /service/application/catalog/v1.0/collections/.","schema":{"type":"string"},"required":true}]}""", slug=slug, f=f, filters=filters, sort_on=sort_on, page_id=page_id, page_size=page_size)
        query_string = await create_query_string(slug=slug, f=f, filters=filters, sort_on=sort_on, page_id=page_id, page_size=page_size)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getCollectionItemsBySlug"]).netloc, "get", await create_url_without_domain("/service/application/catalog/v1.0/collections/{slug}/items/", slug=slug, f=f, filters=filters, sort_on=sort_on, page_id=page_id, page_size=page_size), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getCollectionDetailBySlug(self, slug=None, body=""):
        """Get the details of a collection by its `slug`.
        :param slug : A short, human-readable, URL-friendly identifier of a collection. You can get slug value from the endpoint /service/application/catalog/v1.0/collections/. : type string
        """
        payload = {}
        
        if slug:
            payload["slug"] = slug
        
        # Parameter validation
        schema = CatalogValidator.getCollectionDetailBySlug()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getCollectionDetailBySlug"], proccessed_params="""{"required":[{"in":"path","name":"slug","description":"A short, human-readable, URL-friendly identifier of a collection. You can get slug value from the endpoint /service/application/catalog/v1.0/collections/.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"slug","description":"A short, human-readable, URL-friendly identifier of a collection. You can get slug value from the endpoint /service/application/catalog/v1.0/collections/.","schema":{"type":"string"},"required":true}]}""", slug=slug)
        query_string = await create_query_string(slug=slug)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getCollectionDetailBySlug"]).netloc, "get", await create_url_without_domain("/service/application/catalog/v1.0/collections/{slug}/", slug=slug), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getFollowedListing(self, collection_type=None, page_id=None, page_size=None, body=""):
        """Users can follow a product they like. This API retrieves the products the user have followed.
        :param collection_type : Type of collection followed, i.e. products, brands, or collections. : type string
        :param page_id : Page ID to retrieve next set of results. : type string
        :param page_size : Page ID to retrieve next set of results. : type integer
        """
        payload = {}
        
        if collection_type:
            payload["collection_type"] = collection_type
        
        if page_id:
            payload["page_id"] = page_id
        
        if page_size:
            payload["page_size"] = page_size
        
        # Parameter validation
        schema = CatalogValidator.getFollowedListing()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getFollowedListing"], proccessed_params="""{"required":[{"in":"path","name":"collection_type","description":"Type of collection followed, i.e. products, brands, or collections.","schema":{"type":"string"},"required":true}],"optional":[{"in":"query","name":"page_id","description":"Page ID to retrieve next set of results.","schema":{"type":"string","default":1},"required":false},{"in":"query","name":"page_size","description":"Page ID to retrieve next set of results.","schema":{"type":"integer","default":12},"required":false}],"query":[{"in":"query","name":"page_id","description":"Page ID to retrieve next set of results.","schema":{"type":"string","default":1},"required":false},{"in":"query","name":"page_size","description":"Page ID to retrieve next set of results.","schema":{"type":"integer","default":12},"required":false}],"headers":[],"path":[{"in":"path","name":"collection_type","description":"Type of collection followed, i.e. products, brands, or collections.","schema":{"type":"string"},"required":true}]}""", collection_type=collection_type, page_id=page_id, page_size=page_size)
        query_string = await create_query_string(collection_type=collection_type, page_id=page_id, page_size=page_size)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getFollowedListing"]).netloc, "get", await create_url_without_domain("/service/application/catalog/v1.0/follow/{collection_type}/", collection_type=collection_type, page_id=page_id, page_size=page_size), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def unfollowById(self, collection_type=None, collection_id=None, body=""):
        """You can undo a followed product, brand or collection by its ID. This action is referred as _unfollow_.
        :param collection_type : Type of collection followed, i.e. products, brands, or collections. : type string
        :param collection_id : The ID of the collection type. : type string
        """
        payload = {}
        
        if collection_type:
            payload["collection_type"] = collection_type
        
        if collection_id:
            payload["collection_id"] = collection_id
        
        # Parameter validation
        schema = CatalogValidator.unfollowById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["unfollowById"], proccessed_params="""{"required":[{"in":"path","name":"collection_type","description":"Type of collection followed, i.e. products, brands, or collections.","schema":{"type":"string"},"required":true},{"in":"path","name":"collection_id","description":"The ID of the collection type.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"collection_type","description":"Type of collection followed, i.e. products, brands, or collections.","schema":{"type":"string"},"required":true},{"in":"path","name":"collection_id","description":"The ID of the collection type.","schema":{"type":"string"},"required":true}]}""", collection_type=collection_type, collection_id=collection_id)
        query_string = await create_query_string(collection_type=collection_type, collection_id=collection_id)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["unfollowById"]).netloc, "delete", await create_url_without_domain("/service/application/catalog/v1.0/follow/{collection_type}/{collection_id}/", collection_type=collection_type, collection_id=collection_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def followById(self, collection_type=None, collection_id=None, body=""):
        """Follow a particular entity such as product, brand, collection specified by its ID.
        :param collection_type : Type of collection followed, i.e. products, brands, or collections. : type string
        :param collection_id : The ID of the collection type. : type string
        """
        payload = {}
        
        if collection_type:
            payload["collection_type"] = collection_type
        
        if collection_id:
            payload["collection_id"] = collection_id
        
        # Parameter validation
        schema = CatalogValidator.followById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["followById"], proccessed_params="""{"required":[{"in":"path","name":"collection_type","description":"Type of collection followed, i.e. products, brands, or collections.","schema":{"type":"string"},"required":true},{"in":"path","name":"collection_id","description":"The ID of the collection type.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"collection_type","description":"Type of collection followed, i.e. products, brands, or collections.","schema":{"type":"string"},"required":true},{"in":"path","name":"collection_id","description":"The ID of the collection type.","schema":{"type":"string"},"required":true}]}""", collection_type=collection_type, collection_id=collection_id)
        query_string = await create_query_string(collection_type=collection_type, collection_id=collection_id)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["followById"]).netloc, "post", await create_url_without_domain("/service/application/catalog/v1.0/follow/{collection_type}/{collection_id}/", collection_type=collection_type, collection_id=collection_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getFollowerCountById(self, collection_type=None, collection_id=None, body=""):
        """Get the total count of followers for a given collection type and collection ID.
        :param collection_type : Type of collection, i.e. products, brands, or collections. : type string
        :param collection_id : The ID of the collection type. : type string
        """
        payload = {}
        
        if collection_type:
            payload["collection_type"] = collection_type
        
        if collection_id:
            payload["collection_id"] = collection_id
        
        # Parameter validation
        schema = CatalogValidator.getFollowerCountById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getFollowerCountById"], proccessed_params="""{"required":[{"in":"path","name":"collection_type","description":"Type of collection, i.e. products, brands, or collections.","schema":{"type":"string"},"required":true},{"in":"path","name":"collection_id","description":"The ID of the collection type.","schema":{"type":"string"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"collection_type","description":"Type of collection, i.e. products, brands, or collections.","schema":{"type":"string"},"required":true},{"in":"path","name":"collection_id","description":"The ID of the collection type.","schema":{"type":"string"},"required":true}]}""", collection_type=collection_type, collection_id=collection_id)
        query_string = await create_query_string(collection_type=collection_type, collection_id=collection_id)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getFollowerCountById"]).netloc, "get", await create_url_without_domain("/service/application/catalog/v1.0/follow/{collection_type}/{collection_id}/count/", collection_type=collection_type, collection_id=collection_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getFollowIds(self, collection_type=None, body=""):
        """You can get the IDs of all the followed Products, Brands and Collections. Pass collection_type as query parameter to fetch specific Ids
        :param collection_type : Type of collection, i.e. products, brands, collections. : type string
        """
        payload = {}
        
        if collection_type:
            payload["collection_type"] = collection_type
        
        # Parameter validation
        schema = CatalogValidator.getFollowIds()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getFollowIds"], proccessed_params="""{"required":[],"optional":[{"in":"query","name":"collection_type","description":"Type of collection, i.e. products, brands, collections.","schema":{"type":"string"},"required":false}],"query":[{"in":"query","name":"collection_type","description":"Type of collection, i.e. products, brands, collections.","schema":{"type":"string"},"required":false}],"headers":[],"path":[]}""", collection_type=collection_type)
        query_string = await create_query_string(collection_type=collection_type)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getFollowIds"]).netloc, "get", await create_url_without_domain("/service/application/catalog/v1.0/follow/ids/", collection_type=collection_type), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getStores(self, page_no=None, page_size=None, q=None, city=None, range=None, latitude=None, longitude=None, body=""):
        """Use this API to get a list of stores in a specific application.
        :param page_no : The page number to navigate through the given set of results. : type integer
        :param page_size : Number of items to retrieve in each page. : type integer
        :param q : Search a store by its name or store_code. : type string
        :param city : Search stores by the city in which they are situated. : type string
        :param range : Use this to retrieve stores within a particular range in meters, e.g. 10000, to indicate a 10km range : type integer
        :param latitude : Latitude of the location from where one wants to retreive the nearest stores, e.g. 72.8691788 : type number
        :param longitude : Longitude of the location from where one wants to retreive the nearest stores, e.g. 19.1174114 : type number
        """
        payload = {}
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        
        if q:
            payload["q"] = q
        
        if city:
            payload["city"] = city
        
        if range:
            payload["range"] = range
        
        if latitude:
            payload["latitude"] = latitude
        
        if longitude:
            payload["longitude"] = longitude
        
        # Parameter validation
        schema = CatalogValidator.getStores()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getStores"], proccessed_params="""{"required":[],"optional":[{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results.","schema":{"type":"integer","default":1},"required":false},{"in":"query","name":"page_size","description":"Number of items to retrieve in each page.","schema":{"type":"integer","default":12},"required":false},{"in":"query","name":"q","description":"Search a store by its name or store_code.","schema":{"type":"string"},"required":false},{"in":"query","name":"city","description":"Search stores by the city in which they are situated.","schema":{"type":"string"},"required":false},{"in":"query","name":"range","description":"Use this to retrieve stores within a particular range in meters, e.g. 10000, to indicate a 10km range","schema":{"type":"integer","default":20000},"required":false},{"in":"query","name":"latitude","description":"Latitude of the location from where one wants to retreive the nearest stores, e.g. 72.8691788","schema":{"type":"number"},"required":false},{"in":"query","name":"longitude","description":"Longitude of the location from where one wants to retreive the nearest stores, e.g. 19.1174114","schema":{"type":"number"},"required":false}],"query":[{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results.","schema":{"type":"integer","default":1},"required":false},{"in":"query","name":"page_size","description":"Number of items to retrieve in each page.","schema":{"type":"integer","default":12},"required":false},{"in":"query","name":"q","description":"Search a store by its name or store_code.","schema":{"type":"string"},"required":false},{"in":"query","name":"city","description":"Search stores by the city in which they are situated.","schema":{"type":"string"},"required":false},{"in":"query","name":"range","description":"Use this to retrieve stores within a particular range in meters, e.g. 10000, to indicate a 10km range","schema":{"type":"integer","default":20000},"required":false},{"in":"query","name":"latitude","description":"Latitude of the location from where one wants to retreive the nearest stores, e.g. 72.8691788","schema":{"type":"number"},"required":false},{"in":"query","name":"longitude","description":"Longitude of the location from where one wants to retreive the nearest stores, e.g. 19.1174114","schema":{"type":"number"},"required":false}],"headers":[],"path":[]}""", page_no=page_no, page_size=page_size, q=q, city=city, range=range, latitude=latitude, longitude=longitude)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, q=q, city=city, range=range, latitude=latitude, longitude=longitude)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getStores"]).netloc, "get", await create_url_without_domain("/service/application/catalog/v1.0/locations/", page_no=page_no, page_size=page_size, q=q, city=city, range=range, latitude=latitude, longitude=longitude), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getInStockLocations(self, page_no=None, page_size=None, q=None, city=None, range=None, latitude=None, longitude=None, body=""):
        """Use this API to get a list of stores in a specific application.
        :param page_no : The page number to navigate through the given set of results. : type integer
        :param page_size : Number of items to retrieve in each page. : type integer
        :param q : Search a store by its name or store_code. : type string
        :param city : Search stores by the city in which they are situated. : type string
        :param range : Use this to retrieve stores within a particular range in meters, e.g. 10000, to indicate a 10km range : type integer
        :param latitude : Latitude of the location from where one wants to retreive the nearest stores, e.g. 72.8691788 : type number
        :param longitude : Longitude of the location from where one wants to retreive the nearest stores, e.g. 19.1174114 : type number
        """
        payload = {}
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        
        if q:
            payload["q"] = q
        
        if city:
            payload["city"] = city
        
        if range:
            payload["range"] = range
        
        if latitude:
            payload["latitude"] = latitude
        
        if longitude:
            payload["longitude"] = longitude
        
        # Parameter validation
        schema = CatalogValidator.getInStockLocations()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getInStockLocations"], proccessed_params="""{"required":[],"optional":[{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results.","schema":{"type":"integer","default":1},"required":false},{"in":"query","name":"page_size","description":"Number of items to retrieve in each page.","schema":{"type":"integer","default":12},"required":false},{"in":"query","name":"q","description":"Search a store by its name or store_code.","schema":{"type":"string"},"required":false},{"in":"query","name":"city","description":"Search stores by the city in which they are situated.","schema":{"type":"string"},"required":false},{"in":"query","name":"range","description":"Use this to retrieve stores within a particular range in meters, e.g. 10000, to indicate a 10km range","schema":{"type":"integer","default":20000},"required":false},{"in":"query","name":"latitude","description":"Latitude of the location from where one wants to retreive the nearest stores, e.g. 72.8691788","schema":{"type":"number"},"required":false},{"in":"query","name":"longitude","description":"Longitude of the location from where one wants to retreive the nearest stores, e.g. 19.1174114","schema":{"type":"number"},"required":false}],"query":[{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results.","schema":{"type":"integer","default":1},"required":false},{"in":"query","name":"page_size","description":"Number of items to retrieve in each page.","schema":{"type":"integer","default":12},"required":false},{"in":"query","name":"q","description":"Search a store by its name or store_code.","schema":{"type":"string"},"required":false},{"in":"query","name":"city","description":"Search stores by the city in which they are situated.","schema":{"type":"string"},"required":false},{"in":"query","name":"range","description":"Use this to retrieve stores within a particular range in meters, e.g. 10000, to indicate a 10km range","schema":{"type":"integer","default":20000},"required":false},{"in":"query","name":"latitude","description":"Latitude of the location from where one wants to retreive the nearest stores, e.g. 72.8691788","schema":{"type":"number"},"required":false},{"in":"query","name":"longitude","description":"Longitude of the location from where one wants to retreive the nearest stores, e.g. 19.1174114","schema":{"type":"number"},"required":false}],"headers":[],"path":[]}""", page_no=page_no, page_size=page_size, q=q, city=city, range=range, latitude=latitude, longitude=longitude)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, q=q, city=city, range=range, latitude=latitude, longitude=longitude)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getInStockLocations"]).netloc, "get", await create_url_without_domain("/service/application/catalog/v1.0/in-stock/locations/", page_no=page_no, page_size=page_size, q=q, city=city, range=range, latitude=latitude, longitude=longitude), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getLocationDetailsById(self, location_id=None, body=""):
        """Use this API to get meta details for a store.
        :param location_id : Unique Location ID. : type integer
        """
        payload = {}
        
        if location_id:
            payload["location_id"] = location_id
        
        # Parameter validation
        schema = CatalogValidator.getLocationDetailsById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getLocationDetailsById"], proccessed_params="""{"required":[{"in":"path","name":"location_id","description":"Unique Location ID.","schema":{"type":"integer"},"required":true}],"optional":[],"query":[],"headers":[],"path":[{"in":"path","name":"location_id","description":"Unique Location ID.","schema":{"type":"integer"},"required":true}]}""", location_id=location_id)
        query_string = await create_query_string(location_id=location_id)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getLocationDetailsById"]).netloc, "get", await create_url_without_domain("/service/application/catalog/v1.0/locations/{location_id}/", location_id=location_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getProductBundlesBySlug(self, slug=None, id=None, body=""):
        """Use this API to retrieve products bundles to the one specified by its slug.
        :param slug : Product slug for which bundles need to be fetched. : type string
        :param id : Product uid : type string
        """
        payload = {}
        
        if slug:
            payload["slug"] = slug
        
        if id:
            payload["id"] = id
        
        # Parameter validation
        schema = CatalogValidator.getProductBundlesBySlug()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getProductBundlesBySlug"], proccessed_params="""{"required":[],"optional":[{"in":"query","name":"slug","description":"Product slug for which bundles need to be fetched.","schema":{"type":"string"},"required":false},{"in":"query","name":"id","description":"Product uid","schema":{"type":"string"},"required":false}],"query":[{"in":"query","name":"slug","description":"Product slug for which bundles need to be fetched.","schema":{"type":"string"},"required":false},{"in":"query","name":"id","description":"Product uid","schema":{"type":"string"},"required":false}],"headers":[],"path":[]}""", slug=slug, id=id)
        query_string = await create_query_string(slug=slug, id=id)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getProductBundlesBySlug"]).netloc, "get", await create_url_without_domain("/service/application/catalog/v1.0/product-grouping/", slug=slug, id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getProductPriceBySlug(self, slug=None, size=None, store_id=None, pincode=None, body=""):
        """Prices may vary for different sizes of a product. Use this API to retrieve the price of a product size at all the selling locations near to a PIN Code.
        :param slug : A short, human-readable, URL-friendly identifier of a product. You can get slug value from the endpoint /service/application/catalog/v1.0/products/ : type string
        :param size : A string indicating the size of the product, e.g. S, M, XL. You can get slug value from the endpoint /service/application/catalog/v1.0/products/sizes : type string
        :param store_id : The ID of the store that is selling the product, e.g. 1,2,3. : type integer
        :param pincode : The PIN Code of the area near which the selling locations should be searched, e.g. 400059. : type string
        """
        payload = {}
        
        if slug:
            payload["slug"] = slug
        
        if size:
            payload["size"] = size
        
        if store_id:
            payload["store_id"] = store_id
        
        if pincode:
            payload["pincode"] = pincode
        
        # Parameter validation
        schema = CatalogValidator.getProductPriceBySlug()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getProductPriceBySlug"], proccessed_params="""{"required":[{"in":"path","name":"slug","description":"A short, human-readable, URL-friendly identifier of a product. You can get slug value from the endpoint /service/application/catalog/v1.0/products/","schema":{"type":"string"},"required":true},{"in":"path","name":"size","description":"A string indicating the size of the product, e.g. S, M, XL. You can get slug value from the endpoint /service/application/catalog/v1.0/products/sizes","schema":{"type":"string"},"required":true}],"optional":[{"in":"query","name":"store_id","description":"The ID of the store that is selling the product, e.g. 1,2,3.","schema":{"type":"integer"},"required":false},{"in":"query","name":"pincode","description":"The PIN Code of the area near which the selling locations should be searched, e.g. 400059.","schema":{"type":"string"},"required":false}],"query":[{"in":"query","name":"store_id","description":"The ID of the store that is selling the product, e.g. 1,2,3.","schema":{"type":"integer"},"required":false},{"in":"query","name":"pincode","description":"The PIN Code of the area near which the selling locations should be searched, e.g. 400059.","schema":{"type":"string"},"required":false}],"headers":[],"path":[{"in":"path","name":"slug","description":"A short, human-readable, URL-friendly identifier of a product. You can get slug value from the endpoint /service/application/catalog/v1.0/products/","schema":{"type":"string"},"required":true},{"in":"path","name":"size","description":"A string indicating the size of the product, e.g. S, M, XL. You can get slug value from the endpoint /service/application/catalog/v1.0/products/sizes","schema":{"type":"string"},"required":true}]}""", slug=slug, size=size, store_id=store_id, pincode=pincode)
        query_string = await create_query_string(slug=slug, size=size, store_id=store_id, pincode=pincode)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getProductPriceBySlug"]).netloc, "get", await create_url_without_domain("/service/application/catalog/v2.0/products/{slug}/sizes/{size}/price/", slug=slug, size=size, store_id=store_id, pincode=pincode), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getProductSellersBySlug(self, slug=None, size=None, pincode=None, strategy=None, page_no=None, page_size=None, body=""):
        """A product of a particular size may be sold by multiple sellers. Use this API to fetch the sellers having the stock of a particular size at a given PIN Code.
        :param slug : A short, human-readable, URL-friendly identifier of a product. You can get slug value from the endpoint /service/application/catalog/v1.0/products/ : type string
        :param size : A string indicating the size of the product, e.g. S, M, XL. You can get slug value from the endpoint /service/application/catalog/v1.0/products/sizes : type string
        :param pincode : The 6-digit PIN Code of the area near which the selling locations should be searched, e.g. 400059 : type string
        :param strategy : Sort stores on the basis of strategy. eg, fast-delivery, low-price, optimal. : type string
        :param page_no : The page number to navigate through the given set of results. : type integer
        :param page_size : The number of items to retrieve in each page. : type integer
        """
        payload = {}
        
        if slug:
            payload["slug"] = slug
        
        if size:
            payload["size"] = size
        
        if pincode:
            payload["pincode"] = pincode
        
        if strategy:
            payload["strategy"] = strategy
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        
        # Parameter validation
        schema = CatalogValidator.getProductSellersBySlug()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getProductSellersBySlug"], proccessed_params="""{"required":[{"in":"path","name":"slug","description":"A short, human-readable, URL-friendly identifier of a product. You can get slug value from the endpoint /service/application/catalog/v1.0/products/","schema":{"type":"string"},"required":true},{"in":"path","name":"size","description":"A string indicating the size of the product, e.g. S, M, XL. You can get slug value from the endpoint /service/application/catalog/v1.0/products/sizes","schema":{"type":"string"},"required":true}],"optional":[{"in":"query","name":"pincode","description":"The 6-digit PIN Code of the area near which the selling locations should be searched, e.g. 400059","schema":{"type":"string"},"required":false},{"in":"query","name":"strategy","description":"Sort stores on the basis of strategy. eg, fast-delivery, low-price, optimal.","schema":{"type":"string"}},{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results.","schema":{"type":"integer","default":1},"required":false},{"in":"query","name":"page_size","description":"The number of items to retrieve in each page.","schema":{"type":"integer","default":12},"required":false}],"query":[{"in":"query","name":"pincode","description":"The 6-digit PIN Code of the area near which the selling locations should be searched, e.g. 400059","schema":{"type":"string"},"required":false},{"in":"query","name":"strategy","description":"Sort stores on the basis of strategy. eg, fast-delivery, low-price, optimal.","schema":{"type":"string"}},{"in":"query","name":"page_no","description":"The page number to navigate through the given set of results.","schema":{"type":"integer","default":1},"required":false},{"in":"query","name":"page_size","description":"The number of items to retrieve in each page.","schema":{"type":"integer","default":12},"required":false}],"headers":[],"path":[{"in":"path","name":"slug","description":"A short, human-readable, URL-friendly identifier of a product. You can get slug value from the endpoint /service/application/catalog/v1.0/products/","schema":{"type":"string"},"required":true},{"in":"path","name":"size","description":"A string indicating the size of the product, e.g. S, M, XL. You can get slug value from the endpoint /service/application/catalog/v1.0/products/sizes","schema":{"type":"string"},"required":true}]}""", slug=slug, size=size, pincode=pincode, strategy=strategy, page_no=page_no, page_size=page_size)
        query_string = await create_query_string(slug=slug, size=size, pincode=pincode, strategy=strategy, page_no=page_no, page_size=page_size)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getProductSellersBySlug"]).netloc, "get", await create_url_without_domain("/service/application/catalog/v2.0/products/{slug}/sizes/{size}/sellers/", slug=slug, size=size, pincode=pincode, strategy=strategy, page_no=page_no, page_size=page_size), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    

class Cart:
    def __init__(self, config):
        self._conf = config
        self._relativeUrls = {
            "getCart": "/service/application/cart/v1.0/detail",
            "getCartLastModified": "/service/application/cart/v1.0/detail",
            "addItems": "/service/application/cart/v1.0/detail",
            "updateCart": "/service/application/cart/v1.0/detail",
            "getItemCount": "/service/application/cart/v1.0/basic",
            "getCoupons": "/service/application/cart/v1.0/coupon",
            "applyCoupon": "/service/application/cart/v1.0/coupon",
            "removeCoupon": "/service/application/cart/v1.0/coupon",
            "getBulkDiscountOffers": "/service/application/cart/v1.0/bulk-price",
            "applyRewardPoints": "/service/application/cart/v1.0/redeem/points/",
            "getAddresses": "/service/application/cart/v1.0/address",
            "addAddress": "/service/application/cart/v1.0/address",
            "getAddressById": "/service/application/cart/v1.0/address/{id}",
            "updateAddress": "/service/application/cart/v1.0/address/{id}",
            "removeAddress": "/service/application/cart/v1.0/address/{id}",
            "selectAddress": "/service/application/cart/v1.0/select-address",
            "selectPaymentMode": "/service/application/cart/v1.0/payment",
            "validateCouponForPayment": "/service/application/cart/v1.0/payment/validate/",
            "getShipments": "/service/application/cart/v1.0/shipment",
            "checkoutCart": "/service/application/cart/v1.0/checkout",
            "updateCartMeta": "/service/application/cart/v1.0/meta",
            "getCartShareLink": "/service/application/cart/v1.0/share-cart",
            "getCartSharedItems": "/service/application/cart/v1.0/share-cart/{token}",
            "updateCartWithSharedItems": "/service/application/cart/v1.0/share-cart/{token}/{action}",
            "getPromotionOffers": "/service/application/cart/v1.0/available-promotions",
            "getLadderOffers": "/service/application/cart/v1.0/available-ladder-prices"
            
        }
        self._urls = {
            method: f"{self._conf.domain}{path}" for method, path in self._relativeUrls.items()
        }

    async def updateUrls(self, urls):
        self._urls.update(urls)
    
    async def getCart(self, id=None, i=None, b=None, assign_card_id=None, body=""):
        """Use this API to get details of all the items added to a cart.
        :param id :  : type string
        :param i :  : type boolean
        :param b :  : type boolean
        :param assign_card_id :  : type integer
        """
        payload = {}
        
        if id:
            payload["id"] = id
        
        if i:
            payload["i"] = i
        
        if b:
            payload["b"] = b
        
        if assign_card_id:
            payload["assign_card_id"] = assign_card_id
        
        # Parameter validation
        schema = CartValidator.getCart()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getCart"], proccessed_params="""{"required":[],"optional":[{"in":"query","name":"id","schema":{"type":"string","description":"The unique identifier of the cart"}},{"in":"query","name":"i","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to retrieve all the items added in the cart."}},{"in":"query","name":"b","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to retrieve the price breakup of cart items."}},{"in":"query","name":"assign_card_id","schema":{"type":"integer","description":"Token of user's debit or credit card"}}],"query":[{"in":"query","name":"id","schema":{"type":"string","description":"The unique identifier of the cart"}},{"in":"query","name":"i","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to retrieve all the items added in the cart."}},{"in":"query","name":"b","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to retrieve the price breakup of cart items."}},{"in":"query","name":"assign_card_id","schema":{"type":"integer","description":"Token of user's debit or credit card"}}],"headers":[],"path":[]}""", id=id, i=i, b=b, assign_card_id=assign_card_id)
        query_string = await create_query_string(id=id, i=i, b=b, assign_card_id=assign_card_id)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getCart"]).netloc, "get", await create_url_without_domain("/service/application/cart/v1.0/detail", id=id, i=i, b=b, assign_card_id=assign_card_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getCartLastModified(self, id=None, body=""):
        """Use this API to fetch Last-Modified timestamp in header metadata.
        :param id :  : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        
        # Parameter validation
        schema = CartValidator.getCartLastModified()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getCartLastModified"], proccessed_params="""{"required":[],"optional":[{"in":"query","name":"id","schema":{"type":"string","description":"The unique identifier of the cart"}}],"query":[{"in":"query","name":"id","schema":{"type":"string","description":"The unique identifier of the cart"}}],"headers":[],"path":[]}""", id=id)
        query_string = await create_query_string(id=id)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("HEAD", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getCartLastModified"]).netloc, "head", await create_url_without_domain("/service/application/cart/v1.0/detail", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def addItems(self, i=None, b=None, body=""):
        """Use this API to add items to the cart.
        :param i :  : type boolean
        :param b :  : type boolean
        """
        payload = {}
        
        if i:
            payload["i"] = i
        
        if b:
            payload["b"] = b
        
        # Parameter validation
        schema = CartValidator.addItems()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.AddCartRequest import AddCartRequest
        schema = AddCartRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["addItems"], proccessed_params="""{"required":[],"optional":[{"in":"query","name":"i","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to retrieve all the items added in the cart."}},{"in":"query","name":"b","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to retrieve the price breakup of cart items."}}],"query":[{"in":"query","name":"i","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to retrieve all the items added in the cart."}},{"in":"query","name":"b","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to retrieve the price breakup of cart items."}}],"headers":[],"path":[]}""", i=i, b=b)
        query_string = await create_query_string(i=i, b=b)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["addItems"]).netloc, "post", await create_url_without_domain("/service/application/cart/v1.0/detail", i=i, b=b), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def updateCart(self, id=None, i=None, b=None, body=""):
        """<p>Use this API to update items added to the cart with the help of a request object containing attributes like item_quantity and item_size. These attributes will be fetched from the following APIs</p> <ul> <li><font color="monochrome">operation</font> Operation for current api call. <b>update_item</b> for update items. <b>remove_item</b> for removing items.</li> <li> <font color="monochrome">item_id</font>  "/platform/content/v1/products/"</li> <li> <font color="monochrome">item_size</font>   "/platform/content/v1/products/:slug/sizes/"</li> <li> <font color="monochrome">quantity</font>  item quantity (must be greater than or equal to 1)</li> <li> <font color="monochrome">article_id</font>   "/content​/v1​/products​/:identifier​/sizes​/price​/"</li> <li> <font color="monochrome">item_index</font>  item position in the cart (must be greater than or equal to 0)</li> </ul>
        :param id :  : type string
        :param i :  : type boolean
        :param b :  : type boolean
        """
        payload = {}
        
        if id:
            payload["id"] = id
        
        if i:
            payload["i"] = i
        
        if b:
            payload["b"] = b
        
        # Parameter validation
        schema = CartValidator.updateCart()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.UpdateCartRequest import UpdateCartRequest
        schema = UpdateCartRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["updateCart"], proccessed_params="""{"required":[],"optional":[{"in":"query","name":"id","schema":{"type":"string","description":"The unique identifier of the cart"}},{"in":"query","name":"i","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to retrieve all the items added in the cart."}},{"in":"query","name":"b","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to retrieve the price breakup of cart items."}}],"query":[{"in":"query","name":"id","schema":{"type":"string","description":"The unique identifier of the cart"}},{"in":"query","name":"i","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to retrieve all the items added in the cart."}},{"in":"query","name":"b","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to retrieve the price breakup of cart items."}}],"headers":[],"path":[]}""", id=id, i=i, b=b)
        query_string = await create_query_string(id=id, i=i, b=b)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["updateCart"]).netloc, "put", await create_url_without_domain("/service/application/cart/v1.0/detail", id=id, i=i, b=b), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getItemCount(self, id=None, body=""):
        """Use this API to get the total number of items present in cart.
        :param id : The unique identifier of the cart. : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        
        # Parameter validation
        schema = CartValidator.getItemCount()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getItemCount"], proccessed_params="""{"required":[],"optional":[{"name":"id","in":"query","description":"The unique identifier of the cart.","schema":{"type":"string"}}],"query":[{"name":"id","in":"query","description":"The unique identifier of the cart.","schema":{"type":"string"}}],"headers":[],"path":[]}""", id=id)
        query_string = await create_query_string(id=id)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getItemCount"]).netloc, "get", await create_url_without_domain("/service/application/cart/v1.0/basic", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getCoupons(self, id=None, body=""):
        """Use this API to get a list of available coupons along with their details.
        :param id :  : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        
        # Parameter validation
        schema = CartValidator.getCoupons()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getCoupons"], proccessed_params="""{"required":[],"optional":[{"in":"query","name":"id","schema":{"type":"string","description":"The unique identifier of the cart."}}],"query":[{"in":"query","name":"id","schema":{"type":"string","description":"The unique identifier of the cart."}}],"headers":[],"path":[]}""", id=id)
        query_string = await create_query_string(id=id)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getCoupons"]).netloc, "get", await create_url_without_domain("/service/application/cart/v1.0/coupon", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def applyCoupon(self, i=None, b=None, p=None, id=None, body=""):
        """Use this API to apply coupons on items in the cart.
        :param i :  : type boolean
        :param b :  : type boolean
        :param p :  : type boolean
        :param id :  : type string
        """
        payload = {}
        
        if i:
            payload["i"] = i
        
        if b:
            payload["b"] = b
        
        if p:
            payload["p"] = p
        
        if id:
            payload["id"] = id
        
        # Parameter validation
        schema = CartValidator.applyCoupon()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.ApplyCouponRequest import ApplyCouponRequest
        schema = ApplyCouponRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["applyCoupon"], proccessed_params="""{"required":[],"optional":[{"in":"query","name":"i","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to retrieve all the items added in the cart."}},{"in":"query","name":"b","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to retrieve the price breakup of cart items."}},{"in":"query","name":"p","schema":{"type":"boolean","description":"This is a boolean value. Select `true` for getting a payment option in response."}},{"in":"query","name":"id","schema":{"type":"string","description":"The unique identifier of the cart"}}],"query":[{"in":"query","name":"i","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to retrieve all the items added in the cart."}},{"in":"query","name":"b","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to retrieve the price breakup of cart items."}},{"in":"query","name":"p","schema":{"type":"boolean","description":"This is a boolean value. Select `true` for getting a payment option in response."}},{"in":"query","name":"id","schema":{"type":"string","description":"The unique identifier of the cart"}}],"headers":[],"path":[]}""", i=i, b=b, p=p, id=id)
        query_string = await create_query_string(i=i, b=b, p=p, id=id)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["applyCoupon"]).netloc, "post", await create_url_without_domain("/service/application/cart/v1.0/coupon", i=i, b=b, p=p, id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def removeCoupon(self, id=None, body=""):
        """Remove Coupon applied on the cart by passing uid in request body.
        :param id : The unique identifier of the cart : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        
        # Parameter validation
        schema = CartValidator.removeCoupon()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["removeCoupon"], proccessed_params="""{"required":[],"optional":[{"name":"id","description":"The unique identifier of the cart","schema":{"type":"string"},"in":"query"}],"query":[{"name":"id","description":"The unique identifier of the cart","schema":{"type":"string"},"in":"query"}],"headers":[],"path":[]}""", id=id)
        query_string = await create_query_string(id=id)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["removeCoupon"]).netloc, "delete", await create_url_without_domain("/service/application/cart/v1.0/coupon", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getBulkDiscountOffers(self, item_id=None, article_id=None, uid=None, slug=None, body=""):
        """Use this API to get a list of applicable offers along with current, next and best offer for given product. Either one of uid, item_id, slug should be present.
        :param item_id : The Item ID of the product : type integer
        :param article_id : Article Mongo ID : type string
        :param uid : UID of the product : type integer
        :param slug : A short, human-readable, URL-friendly identifier of a product. You can get slug value from the endpoint /service/application/catalog/v1.0/products/ : type string
        """
        payload = {}
        
        if item_id:
            payload["item_id"] = item_id
        
        if article_id:
            payload["article_id"] = article_id
        
        if uid:
            payload["uid"] = uid
        
        if slug:
            payload["slug"] = slug
        
        # Parameter validation
        schema = CartValidator.getBulkDiscountOffers()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getBulkDiscountOffers"], proccessed_params="""{"required":[],"optional":[{"name":"item_id","description":"The Item ID of the product","in":"query","schema":{"type":"integer"}},{"name":"article_id","description":"Article Mongo ID","in":"query","schema":{"type":"string"}},{"name":"uid","description":"UID of the product","in":"query","schema":{"type":"integer"}},{"name":"slug","description":"A short, human-readable, URL-friendly identifier of a product. You can get slug value from the endpoint /service/application/catalog/v1.0/products/","in":"query","schema":{"type":"string"}}],"query":[{"name":"item_id","description":"The Item ID of the product","in":"query","schema":{"type":"integer"}},{"name":"article_id","description":"Article Mongo ID","in":"query","schema":{"type":"string"}},{"name":"uid","description":"UID of the product","in":"query","schema":{"type":"integer"}},{"name":"slug","description":"A short, human-readable, URL-friendly identifier of a product. You can get slug value from the endpoint /service/application/catalog/v1.0/products/","in":"query","schema":{"type":"string"}}],"headers":[],"path":[]}""", item_id=item_id, article_id=article_id, uid=uid, slug=slug)
        query_string = await create_query_string(item_id=item_id, article_id=article_id, uid=uid, slug=slug)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getBulkDiscountOffers"]).netloc, "get", await create_url_without_domain("/service/application/cart/v1.0/bulk-price", item_id=item_id, article_id=article_id, uid=uid, slug=slug), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def applyRewardPoints(self, id=None, i=None, b=None, body=""):
        """Use this API to redeem a fixed no. of reward points by applying it to the cart.
        :param id :  : type string
        :param i :  : type boolean
        :param b :  : type boolean
        """
        payload = {}
        
        if id:
            payload["id"] = id
        
        if i:
            payload["i"] = i
        
        if b:
            payload["b"] = b
        
        # Parameter validation
        schema = CartValidator.applyRewardPoints()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.RewardPointRequest import RewardPointRequest
        schema = RewardPointRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["applyRewardPoints"], proccessed_params="""{"required":[],"optional":[{"in":"query","name":"id","schema":{"type":"string","description":"The unique identifier of the cart"}},{"in":"query","name":"i","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to retrieve all the items added in the cart."}},{"in":"query","name":"b","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to retrieve the price breakup of cart items."}}],"query":[{"in":"query","name":"id","schema":{"type":"string","description":"The unique identifier of the cart"}},{"in":"query","name":"i","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to retrieve all the items added in the cart."}},{"in":"query","name":"b","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to retrieve the price breakup of cart items."}}],"headers":[],"path":[]}""", id=id, i=i, b=b)
        query_string = await create_query_string(id=id, i=i, b=b)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["applyRewardPoints"]).netloc, "post", await create_url_without_domain("/service/application/cart/v1.0/redeem/points/", id=id, i=i, b=b), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getAddresses(self, cart_id=None, mobile_no=None, checkout_mode=None, tags=None, is_default=None, body=""):
        """Use this API to get all the addresses associated with an account. If successful, returns a Address resource in the response body specified in GetAddressesResponse.attibutes listed below are optional <ul> <li> <font color="monochrome">uid</font></li> <li> <font color="monochrome">address_id</font></li> <li> <font color="monochrome">mobile_no</font></li> <li> <font color="monochrome">checkout_mode</font></li> <li> <font color="monochrome">tags</font></li> <li> <font color="monochrome">default</font></li> </ul>
        :param cart_id :  : type string
        :param mobile_no :  : type string
        :param checkout_mode :  : type string
        :param tags :  : type string
        :param is_default :  : type boolean
        """
        payload = {}
        
        if cart_id:
            payload["cart_id"] = cart_id
        
        if mobile_no:
            payload["mobile_no"] = mobile_no
        
        if checkout_mode:
            payload["checkout_mode"] = checkout_mode
        
        if tags:
            payload["tags"] = tags
        
        if is_default:
            payload["is_default"] = is_default
        
        # Parameter validation
        schema = CartValidator.getAddresses()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getAddresses"], proccessed_params="""{"required":[],"optional":[{"name":"cart_id","in":"query","schema":{"type":"string","description":"The unique identifier of the cart"}},{"in":"query","name":"mobile_no","schema":{"type":"string","description":"10-digit mobile number"}},{"in":"query","name":"checkout_mode","schema":{"type":"string","description":"Option to checkout for self or for others"}},{"in":"query","name":"tags","schema":{"type":"string","description":"Tag given to an address, e.g. work, home, office, shop."}},{"in":"query","name":"is_default","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to fetch the default address."}}],"query":[{"name":"cart_id","in":"query","schema":{"type":"string","description":"The unique identifier of the cart"}},{"in":"query","name":"mobile_no","schema":{"type":"string","description":"10-digit mobile number"}},{"in":"query","name":"checkout_mode","schema":{"type":"string","description":"Option to checkout for self or for others"}},{"in":"query","name":"tags","schema":{"type":"string","description":"Tag given to an address, e.g. work, home, office, shop."}},{"in":"query","name":"is_default","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to fetch the default address."}}],"headers":[],"path":[]}""", cart_id=cart_id, mobile_no=mobile_no, checkout_mode=checkout_mode, tags=tags, is_default=is_default)
        query_string = await create_query_string(cart_id=cart_id, mobile_no=mobile_no, checkout_mode=checkout_mode, tags=tags, is_default=is_default)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getAddresses"]).netloc, "get", await create_url_without_domain("/service/application/cart/v1.0/address", cart_id=cart_id, mobile_no=mobile_no, checkout_mode=checkout_mode, tags=tags, is_default=is_default), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def addAddress(self, body=""):
        """Use this API to add an address to an account.
        """
        payload = {}
        
        # Parameter validation
        schema = CartValidator.addAddress()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.Address import Address
        schema = Address()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["addAddress"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["addAddress"]).netloc, "post", await create_url_without_domain("/service/application/cart/v1.0/address", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getAddressById(self, id=None, cart_id=None, mobile_no=None, checkout_mode=None, tags=None, is_default=None, body=""):
        """Use this API to get an addresses using its ID. If successful, returns a Address resource in the response body specified in `Address`. Attibutes listed below are optional <ul> <li> <font color="monochrome">mobile_no</font></li> <li> <font color="monochrome">checkout_mode</font></li> <li> <font color="monochrome">tags</font></li> <li> <font color="monochrome">default</font></li> </ul>
        :param id :  : type string
        :param cart_id :  : type string
        :param mobile_no :  : type string
        :param checkout_mode :  : type string
        :param tags :  : type string
        :param is_default :  : type boolean
        """
        payload = {}
        
        if id:
            payload["id"] = id
        
        if cart_id:
            payload["cart_id"] = cart_id
        
        if mobile_no:
            payload["mobile_no"] = mobile_no
        
        if checkout_mode:
            payload["checkout_mode"] = checkout_mode
        
        if tags:
            payload["tags"] = tags
        
        if is_default:
            payload["is_default"] = is_default
        
        # Parameter validation
        schema = CartValidator.getAddressById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getAddressById"], proccessed_params="""{"required":[{"name":"id","in":"path","schema":{"type":"string","description":"ID allotted to the selected address"},"required":true}],"optional":[{"name":"cart_id","in":"query","schema":{"type":"string","description":"The unique identifier of the cart"}},{"in":"query","name":"mobile_no","schema":{"type":"string","description":"10-digit mobile number"}},{"in":"query","name":"checkout_mode","schema":{"type":"string","description":"Option to checkout for self or for others"}},{"in":"query","name":"tags","schema":{"type":"string","description":"Tag given to an address, e.g. work, home, office, shop."}},{"in":"query","name":"is_default","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to fetch the default address."}}],"query":[{"name":"cart_id","in":"query","schema":{"type":"string","description":"The unique identifier of the cart"}},{"in":"query","name":"mobile_no","schema":{"type":"string","description":"10-digit mobile number"}},{"in":"query","name":"checkout_mode","schema":{"type":"string","description":"Option to checkout for self or for others"}},{"in":"query","name":"tags","schema":{"type":"string","description":"Tag given to an address, e.g. work, home, office, shop."}},{"in":"query","name":"is_default","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to fetch the default address."}}],"headers":[],"path":[{"name":"id","in":"path","schema":{"type":"string","description":"ID allotted to the selected address"},"required":true}]}""", id=id, cart_id=cart_id, mobile_no=mobile_no, checkout_mode=checkout_mode, tags=tags, is_default=is_default)
        query_string = await create_query_string(id=id, cart_id=cart_id, mobile_no=mobile_no, checkout_mode=checkout_mode, tags=tags, is_default=is_default)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getAddressById"]).netloc, "get", await create_url_without_domain("/service/application/cart/v1.0/address/{id}", id=id, cart_id=cart_id, mobile_no=mobile_no, checkout_mode=checkout_mode, tags=tags, is_default=is_default), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def updateAddress(self, id=None, body=""):
        """<p>Use this API to update an existing address in the account. Request object should contain attributes mentioned in  <font color="blue">Address </font> can be updated. These attributes are:</p> <ul> <li> <font color="monochrome">is_default_address</font></li> <li> <font color="monochrome">landmark</font></li> <li> <font color="monochrome">area</font></li> <li> <font color="monochrome">pincode</font></li> <li> <font color="monochrome">email</font></li> <li> <font color="monochrome">address_type</font></li> <li> <font color="monochrome">name</font></li> <li> <font color="monochrome">address_id</font></li> <li> <font color="monochrome">address</font></li> </ul>
        :param id : ID allotted to the selected address : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        
        # Parameter validation
        schema = CartValidator.updateAddress()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.Address import Address
        schema = Address()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["updateAddress"], proccessed_params="""{"required":[{"name":"id","description":"ID allotted to the selected address","schema":{"type":"string"},"in":"path","required":true}],"optional":[],"query":[],"headers":[],"path":[{"name":"id","description":"ID allotted to the selected address","schema":{"type":"string"},"in":"path","required":true}]}""", id=id)
        query_string = await create_query_string(id=id)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["updateAddress"]).netloc, "put", await create_url_without_domain("/service/application/cart/v1.0/address/{id}", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def removeAddress(self, id=None, body=""):
        """Use this API to delete an address by its ID. This will returns an object that will indicate whether the address was deleted successfully or not.
        :param id : ID allotted to the selected address : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        
        # Parameter validation
        schema = CartValidator.removeAddress()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["removeAddress"], proccessed_params="""{"required":[{"name":"id","description":"ID allotted to the selected address","schema":{"type":"string"},"in":"path","required":true}],"optional":[],"query":[],"headers":[],"path":[{"name":"id","description":"ID allotted to the selected address","schema":{"type":"string"},"in":"path","required":true}]}""", id=id)
        query_string = await create_query_string(id=id)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["removeAddress"]).netloc, "delete", await create_url_without_domain("/service/application/cart/v1.0/address/{id}", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def selectAddress(self, cart_id=None, i=None, b=None, body=""):
        """<p>Select Address from all addresses associated with the account in order to ship the cart items to that address, otherwise default address will be selected implicitly. See `SelectCartAddressRequest` in schema of request body for the list of attributes needed to select Address from account. On successful request, this API returns a Cart object. Below address attributes are required. <ul> <li> <font color="monochrome">address_id</font></li> <li> <font color="monochrome">billing_address_id</font></li> <li> <font color="monochrome">uid</font></li> </ul></p>
        :param cart_id :  : type string
        :param i :  : type boolean
        :param b :  : type boolean
        """
        payload = {}
        
        if cart_id:
            payload["cart_id"] = cart_id
        
        if i:
            payload["i"] = i
        
        if b:
            payload["b"] = b
        
        # Parameter validation
        schema = CartValidator.selectAddress()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.SelectCartAddressRequest import SelectCartAddressRequest
        schema = SelectCartAddressRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["selectAddress"], proccessed_params="""{"required":[],"optional":[{"in":"query","name":"cart_id","schema":{"type":"string","description":"The unique identifier of the cart"}},{"in":"query","name":"i","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to retrieve all the items added in the cart."}},{"in":"query","name":"b","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to retrieve the price breakup of cart items."}}],"query":[{"in":"query","name":"cart_id","schema":{"type":"string","description":"The unique identifier of the cart"}},{"in":"query","name":"i","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to retrieve all the items added in the cart."}},{"in":"query","name":"b","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to retrieve the price breakup of cart items."}}],"headers":[],"path":[]}""", cart_id=cart_id, i=i, b=b)
        query_string = await create_query_string(cart_id=cart_id, i=i, b=b)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["selectAddress"]).netloc, "post", await create_url_without_domain("/service/application/cart/v1.0/select-address", cart_id=cart_id, i=i, b=b), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def selectPaymentMode(self, id=None, body=""):
        """Use this API to update cart payment.
        :param id :  : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        
        # Parameter validation
        schema = CartValidator.selectPaymentMode()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.UpdateCartPaymentRequest import UpdateCartPaymentRequest
        schema = UpdateCartPaymentRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["selectPaymentMode"], proccessed_params="""{"required":[],"optional":[{"in":"query","name":"id","schema":{"type":"string","description":"The unique identifier of the cart"}}],"query":[{"in":"query","name":"id","schema":{"type":"string","description":"The unique identifier of the cart"}}],"headers":[],"path":[]}""", id=id)
        query_string = await create_query_string(id=id)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["selectPaymentMode"]).netloc, "put", await create_url_without_domain("/service/application/cart/v1.0/payment", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def validateCouponForPayment(self, id=None, address_id=None, payment_mode=None, payment_identifier=None, aggregator_name=None, merchant_code=None, body=""):
        """Use this API to validate a coupon against the payment mode such as NetBanking, Wallet, UPI etc.
        :param id :  : type string
        :param address_id :  : type string
        :param payment_mode :  : type string
        :param payment_identifier :  : type string
        :param aggregator_name :  : type string
        :param merchant_code :  : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        
        if address_id:
            payload["address_id"] = address_id
        
        if payment_mode:
            payload["payment_mode"] = payment_mode
        
        if payment_identifier:
            payload["payment_identifier"] = payment_identifier
        
        if aggregator_name:
            payload["aggregator_name"] = aggregator_name
        
        if merchant_code:
            payload["merchant_code"] = merchant_code
        
        # Parameter validation
        schema = CartValidator.validateCouponForPayment()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["validateCouponForPayment"], proccessed_params="""{"required":[],"optional":[{"in":"query","name":"id","schema":{"type":"string","description":"The unique identifier of the cart"}},{"in":"query","name":"address_id","schema":{"type":"string","description":"ID allotted to an address"}},{"in":"query","name":"payment_mode","schema":{"type":"string","description":"Payment mode selected by the customer"}},{"in":"query","name":"payment_identifier","schema":{"type":"string","description":"Identifier of payment like ICIC, PAYTM"}},{"in":"query","name":"aggregator_name","schema":{"type":"string","description":"Payment gateway identifier"}},{"in":"query","name":"merchant_code","schema":{"type":"string","description":"Identifier used by payment gateway for a given payment mode, e.g. NB_ICIC, PAYTM"}}],"query":[{"in":"query","name":"id","schema":{"type":"string","description":"The unique identifier of the cart"}},{"in":"query","name":"address_id","schema":{"type":"string","description":"ID allotted to an address"}},{"in":"query","name":"payment_mode","schema":{"type":"string","description":"Payment mode selected by the customer"}},{"in":"query","name":"payment_identifier","schema":{"type":"string","description":"Identifier of payment like ICIC, PAYTM"}},{"in":"query","name":"aggregator_name","schema":{"type":"string","description":"Payment gateway identifier"}},{"in":"query","name":"merchant_code","schema":{"type":"string","description":"Identifier used by payment gateway for a given payment mode, e.g. NB_ICIC, PAYTM"}}],"headers":[],"path":[]}""", id=id, address_id=address_id, payment_mode=payment_mode, payment_identifier=payment_identifier, aggregator_name=aggregator_name, merchant_code=merchant_code)
        query_string = await create_query_string(id=id, address_id=address_id, payment_mode=payment_mode, payment_identifier=payment_identifier, aggregator_name=aggregator_name, merchant_code=merchant_code)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["validateCouponForPayment"]).netloc, "get", await create_url_without_domain("/service/application/cart/v1.0/payment/validate/", id=id, address_id=address_id, payment_mode=payment_mode, payment_identifier=payment_identifier, aggregator_name=aggregator_name, merchant_code=merchant_code), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getShipments(self, p=None, id=None, address_id=None, area_code=None, body=""):
        """Use this API to get shipment details, expected delivery date, items and price breakup of the shipment.
        :param p : This is a boolean value. Select `true` for getting a payment option in response. : type boolean
        :param id : The unique identifier of the cart : type string
        :param address_id : ID allotted to the selected address : type string
        :param area_code : The PIN Code of the destination address, e.g. 400059 : type string
        """
        payload = {}
        
        if p:
            payload["p"] = p
        
        if id:
            payload["id"] = id
        
        if address_id:
            payload["address_id"] = address_id
        
        if area_code:
            payload["area_code"] = area_code
        
        # Parameter validation
        schema = CartValidator.getShipments()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getShipments"], proccessed_params="""{"required":[],"optional":[{"name":"p","description":"This is a boolean value. Select `true` for getting a payment option in response.","in":"query","schema":{"type":"boolean"}},{"name":"id","description":"The unique identifier of the cart","in":"query","schema":{"type":"string"}},{"name":"address_id","description":"ID allotted to the selected address","in":"query","schema":{"type":"string"}},{"name":"area_code","description":"The PIN Code of the destination address, e.g. 400059","in":"query","schema":{"type":"string"}}],"query":[{"name":"p","description":"This is a boolean value. Select `true` for getting a payment option in response.","in":"query","schema":{"type":"boolean"}},{"name":"id","description":"The unique identifier of the cart","in":"query","schema":{"type":"string"}},{"name":"address_id","description":"ID allotted to the selected address","in":"query","schema":{"type":"string"}},{"name":"area_code","description":"The PIN Code of the destination address, e.g. 400059","in":"query","schema":{"type":"string"}}],"headers":[],"path":[]}""", p=p, id=id, address_id=address_id, area_code=area_code)
        query_string = await create_query_string(p=p, id=id, address_id=address_id, area_code=area_code)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getShipments"]).netloc, "get", await create_url_without_domain("/service/application/cart/v1.0/shipment", p=p, id=id, address_id=address_id, area_code=area_code), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def checkoutCart(self, body=""):
        """Use this API to checkout all items in the cart for payment and order generation. For COD, order will be directly generated, whereas for other checkout modes, user will be redirected to a payment gateway.
        """
        payload = {}
        
        # Parameter validation
        schema = CartValidator.checkoutCart()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.CartCheckoutDetailRequest import CartCheckoutDetailRequest
        schema = CartCheckoutDetailRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["checkoutCart"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["checkoutCart"]).netloc, "post", await create_url_without_domain("/service/application/cart/v1.0/checkout", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def updateCartMeta(self, id=None, body=""):
        """Use this API to update cart meta like checkout_mode and gstin.
        :param id : The unique identifier of the cart : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        
        # Parameter validation
        schema = CartValidator.updateCartMeta()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.CartMetaRequest import CartMetaRequest
        schema = CartMetaRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["updateCartMeta"], proccessed_params="""{"required":[],"optional":[{"name":"id","description":"The unique identifier of the cart","schema":{"type":"string"},"in":"query"}],"query":[{"name":"id","description":"The unique identifier of the cart","schema":{"type":"string"},"in":"query"}],"headers":[],"path":[]}""", id=id)
        query_string = await create_query_string(id=id)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["updateCartMeta"]).netloc, "put", await create_url_without_domain("/service/application/cart/v1.0/meta", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getCartShareLink(self, body=""):
        """Use this API to generate a shared cart snapshot and return a shortlink token. The link can be shared with other users for getting the same items in their cart.
        """
        payload = {}
        
        # Parameter validation
        schema = CartValidator.getCartShareLink()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.GetShareCartLinkRequest import GetShareCartLinkRequest
        schema = GetShareCartLinkRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getCartShareLink"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getCartShareLink"]).netloc, "post", await create_url_without_domain("/service/application/cart/v1.0/share-cart", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getCartSharedItems(self, token=None, body=""):
        """Use this API to get the shared cart details as per the token generated using the share-cart API.
        :param token : Token of the shared short link : type string
        """
        payload = {}
        
        if token:
            payload["token"] = token
        
        # Parameter validation
        schema = CartValidator.getCartSharedItems()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getCartSharedItems"], proccessed_params="""{"required":[{"name":"token","description":"Token of the shared short link","schema":{"type":"string"},"in":"path","required":true}],"optional":[],"query":[],"headers":[],"path":[{"name":"token","description":"Token of the shared short link","schema":{"type":"string"},"in":"path","required":true}]}""", token=token)
        query_string = await create_query_string(token=token)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getCartSharedItems"]).netloc, "get", await create_url_without_domain("/service/application/cart/v1.0/share-cart/{token}", token=token), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def updateCartWithSharedItems(self, token=None, action=None, body=""):
        """Use this API to merge the shared cart with existing cart, or replace the existing cart with the shared cart. The `action` parameter is used to indicate the operation Merge or Replace.
        :param token : Token of the shared short link : type string
        :param action : Operation to perform on the existing cart merge or replace. : type string
        """
        payload = {}
        
        if token:
            payload["token"] = token
        
        if action:
            payload["action"] = action
        
        # Parameter validation
        schema = CartValidator.updateCartWithSharedItems()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["updateCartWithSharedItems"], proccessed_params="""{"required":[{"name":"token","description":"Token of the shared short link","schema":{"type":"string"},"in":"path","required":true},{"name":"action","description":"Operation to perform on the existing cart merge or replace.","schema":{"type":"string","enum":["merge","replace"]},"in":"path","required":true}],"optional":[],"query":[],"headers":[],"path":[{"name":"token","description":"Token of the shared short link","schema":{"type":"string"},"in":"path","required":true},{"name":"action","description":"Operation to perform on the existing cart merge or replace.","schema":{"type":"string","enum":["merge","replace"]},"in":"path","required":true}]}""", token=token, action=action)
        query_string = await create_query_string(token=token, action=action)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["updateCartWithSharedItems"]).netloc, "post", await create_url_without_domain("/service/application/cart/v1.0/share-cart/{token}/{action}", token=token, action=action), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getPromotionOffers(self, slug=None, page_size=None, promotion_group=None, body=""):
        """Use this API to get top 5 offers available for current product
        :param slug : A short, human-readable, URL-friendly identifier of a product. You can get slug value from the endpoint /service/application/catalog/v1.0/products/ : type string
        :param page_size : Number of offers to be fetched to show : type integer
        :param promotion_group : Type of promotion groups : type string
        """
        payload = {}
        
        if slug:
            payload["slug"] = slug
        
        if page_size:
            payload["page_size"] = page_size
        
        if promotion_group:
            payload["promotion_group"] = promotion_group
        
        # Parameter validation
        schema = CartValidator.getPromotionOffers()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getPromotionOffers"], proccessed_params="""{"required":[],"optional":[{"name":"slug","description":"A short, human-readable, URL-friendly identifier of a product. You can get slug value from the endpoint /service/application/catalog/v1.0/products/","in":"query","schema":{"type":"string"}},{"name":"page_size","description":"Number of offers to be fetched to show","in":"query","schema":{"type":"integer"}},{"name":"promotion_group","description":"Type of promotion groups","in":"query","schema":{"type":"string"}}],"query":[{"name":"slug","description":"A short, human-readable, URL-friendly identifier of a product. You can get slug value from the endpoint /service/application/catalog/v1.0/products/","in":"query","schema":{"type":"string"}},{"name":"page_size","description":"Number of offers to be fetched to show","in":"query","schema":{"type":"integer"}},{"name":"promotion_group","description":"Type of promotion groups","in":"query","schema":{"type":"string"}}],"headers":[],"path":[]}""", slug=slug, page_size=page_size, promotion_group=promotion_group)
        query_string = await create_query_string(slug=slug, page_size=page_size, promotion_group=promotion_group)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getPromotionOffers"]).netloc, "get", await create_url_without_domain("/service/application/cart/v1.0/available-promotions", slug=slug, page_size=page_size, promotion_group=promotion_group), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getLadderOffers(self, slug=None, store_id=None, promotion_id=None, page_size=None, body=""):
        """Use this API to get applicable ladder price promotion for current product
        :param slug : A short, human-readable, URL-friendly identifier of a product. You can get slug value from the endpoint /service/application/catalog/v1.0/products/ : type string
        :param store_id : Store uid of assigned store on PDP page. If not passed default first created ladder will be returned : type string
        :param promotion_id : Get ladder information of given promotion id explicitely : type string
        :param page_size : Number of offers to be fetched to show : type integer
        """
        payload = {}
        
        if slug:
            payload["slug"] = slug
        
        if store_id:
            payload["store_id"] = store_id
        
        if promotion_id:
            payload["promotion_id"] = promotion_id
        
        if page_size:
            payload["page_size"] = page_size
        
        # Parameter validation
        schema = CartValidator.getLadderOffers()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getLadderOffers"], proccessed_params="""{"required":[{"name":"slug","description":"A short, human-readable, URL-friendly identifier of a product. You can get slug value from the endpoint /service/application/catalog/v1.0/products/","in":"query","required":true,"schema":{"type":"string"}}],"optional":[{"name":"store_id","description":"Store uid of assigned store on PDP page. If not passed default first created ladder will be returned","in":"query","schema":{"type":"string"}},{"name":"promotion_id","description":"Get ladder information of given promotion id explicitely","in":"query","required":false,"schema":{"type":"string"}},{"name":"page_size","description":"Number of offers to be fetched to show","in":"query","schema":{"type":"integer"}}],"query":[{"name":"slug","description":"A short, human-readable, URL-friendly identifier of a product. You can get slug value from the endpoint /service/application/catalog/v1.0/products/","in":"query","required":true,"schema":{"type":"string"}},{"name":"store_id","description":"Store uid of assigned store on PDP page. If not passed default first created ladder will be returned","in":"query","schema":{"type":"string"}},{"name":"promotion_id","description":"Get ladder information of given promotion id explicitely","in":"query","required":false,"schema":{"type":"string"}},{"name":"page_size","description":"Number of offers to be fetched to show","in":"query","schema":{"type":"integer"}}],"headers":[],"path":[]}""", slug=slug, store_id=store_id, promotion_id=promotion_id, page_size=page_size)
        query_string = await create_query_string(slug=slug, store_id=store_id, promotion_id=promotion_id, page_size=page_size)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getLadderOffers"]).netloc, "get", await create_url_without_domain("/service/application/cart/v1.0/available-ladder-prices", slug=slug, store_id=store_id, promotion_id=promotion_id, page_size=page_size), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    

class Common:
    def __init__(self, config):
        self._conf = config
        self._relativeUrls = {
            "searchApplication": "/service/common/configuration/v1.0/application/search-application",
            "getLocations": "/service/common/configuration/v1.0/location"
            
        }
        self._urls = {
            method: f"{self._conf.domain}{path}" for method, path in self._relativeUrls.items()
        }

    async def updateUrls(self, urls):
        self._urls.update(urls)
    
    async def searchApplication(self, authorization=None, query=None, body=""):
        """Provide application name or domain url
        :param authorization :  : type string
        :param query : Provide application name : type string
        """
        payload = {}
        
        if authorization:
            payload["authorization"] = authorization
        
        if query:
            payload["query"] = query
        
        # Parameter validation
        schema = CommonValidator.searchApplication()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["searchApplication"], proccessed_params="""{"required":[],"optional":[{"in":"header","name":"authorization","schema":{"type":"string"}},{"in":"query","name":"query","schema":{"type":"string"},"description":"Provide application name"}],"query":[{"in":"query","name":"query","schema":{"type":"string"},"description":"Provide application name"}],"headers":[{"in":"header","name":"authorization","schema":{"type":"string"}}],"path":[]}""", authorization=authorization, query=query)
        query_string = await create_query_string(authorization=authorization, query=query)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["searchApplication"]).netloc, "get", await create_url_without_domain("/service/common/configuration/v1.0/application/search-application", authorization=authorization, query=query), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getLocations(self, location_type=None, id=None, body=""):
        """
        :param location_type : Provide location type to query on. Possible values : country, state, city : type string
        :param id : Field is optional when location_type is country. If querying for state, provide id of country. If querying for city, provide id of state. : type string
        """
        payload = {}
        
        if location_type:
            payload["location_type"] = location_type
        
        if id:
            payload["id"] = id
        
        # Parameter validation
        schema = CommonValidator.getLocations()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getLocations"], proccessed_params="""{"required":[],"optional":[{"in":"query","name":"location_type","schema":{"type":"string","enum":["country","state","city"]},"description":"Provide location type to query on. Possible values : country, state, city"},{"in":"query","name":"id","schema":{"type":"string"},"description":"Field is optional when location_type is country. If querying for state, provide id of country. If querying for city, provide id of state."}],"query":[{"in":"query","name":"location_type","schema":{"type":"string","enum":["country","state","city"]},"description":"Provide location type to query on. Possible values : country, state, city"},{"in":"query","name":"id","schema":{"type":"string"},"description":"Field is optional when location_type is country. If querying for state, provide id of country. If querying for city, provide id of state."}],"headers":[],"path":[]}""", location_type=location_type, id=id)
        query_string = await create_query_string(location_type=location_type, id=id)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getLocations"]).netloc, "get", await create_url_without_domain("/service/common/configuration/v1.0/location", location_type=location_type, id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    

class Lead:
    def __init__(self, config):
        self._conf = config
        self._relativeUrls = {
            "getTicket": "/service/application/lead/v1.0/ticket/{id}",
            "createHistory": "/service/application/lead/v1.0/ticket/{id}/history",
            "createTicket": "/service/application/lead/v1.0/ticket/",
            "getCustomForm": "/service/application/lead/v1.0/form/{slug}",
            "submitCustomForm": "/service/application/lead/v1.0/form/{slug}/submit",
            "getParticipantsInsideVideoRoom": "/service/application/lead/v1.0/video/room/{unique_name}/participants",
            "getTokenForVideoRoom": "/service/application/lead/v1.0/video/room/{unique_name}/token"
            
        }
        self._urls = {
            method: f"{self._conf.domain}{path}" for method, path in self._relativeUrls.items()
        }

    async def updateUrls(self, urls):
        self._urls.update(urls)
    
    async def getTicket(self, id=None, body=""):
        """Get Ticket with the specific id, this is used to view the ticket details
        :param id : ID of ticket to be retrieved : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        
        # Parameter validation
        schema = LeadValidator.getTicket()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getTicket"], proccessed_params="""{"required":[{"name":"id","in":"path","description":"ID of ticket to be retrieved","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"id","in":"path","description":"ID of ticket to be retrieved","required":true,"schema":{"type":"string"}}]}""", id=id)
        query_string = await create_query_string(id=id)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getTicket"]).netloc, "get", await create_url_without_domain("/service/application/lead/v1.0/ticket/{id}", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def createHistory(self, id=None, body=""):
        """Create history for specific Ticket, this history is seen on ticket detail page, this can be comment, log or rating.
        :param id : Ticket ID for which history is created : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        
        # Parameter validation
        schema = LeadValidator.createHistory()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.TicketHistoryPayload import TicketHistoryPayload
        schema = TicketHistoryPayload()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["createHistory"], proccessed_params="""{"required":[{"name":"id","in":"path","description":"Ticket ID for which history is created","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"id","in":"path","description":"Ticket ID for which history is created","required":true,"schema":{"type":"string"}}]}""", id=id)
        query_string = await create_query_string(id=id)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["createHistory"]).netloc, "post", await create_url_without_domain("/service/application/lead/v1.0/ticket/{id}/history", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def createTicket(self, body=""):
        """This is used to Create Ticket.
        """
        payload = {}
        
        # Parameter validation
        schema = LeadValidator.createTicket()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.AddTicketPayload import AddTicketPayload
        schema = AddTicketPayload()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["createTicket"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["createTicket"]).netloc, "post", await create_url_without_domain("/service/application/lead/v1.0/ticket/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getCustomForm(self, slug=None, body=""):
        """Get specific Custom Form using it's slug, this is used to view the form.
        :param slug : Slug of form whose response is getting submitted : type string
        """
        payload = {}
        
        if slug:
            payload["slug"] = slug
        
        # Parameter validation
        schema = LeadValidator.getCustomForm()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getCustomForm"], proccessed_params="""{"required":[{"name":"slug","in":"path","description":"Slug of form whose response is getting submitted","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"slug","in":"path","description":"Slug of form whose response is getting submitted","required":true,"schema":{"type":"string"}}]}""", slug=slug)
        query_string = await create_query_string(slug=slug)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getCustomForm"]).netloc, "get", await create_url_without_domain("/service/application/lead/v1.0/form/{slug}", slug=slug), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def submitCustomForm(self, slug=None, body=""):
        """Submit Response for a specific Custom Form using it's slug, this response is then used to create a ticket on behalf of the user.
        :param slug : Slug of form whose response is getting submitted : type string
        """
        payload = {}
        
        if slug:
            payload["slug"] = slug
        
        # Parameter validation
        schema = LeadValidator.submitCustomForm()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.CustomFormSubmissionPayload import CustomFormSubmissionPayload
        schema = CustomFormSubmissionPayload()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["submitCustomForm"], proccessed_params="""{"required":[{"name":"slug","in":"path","description":"Slug of form whose response is getting submitted","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"slug","in":"path","description":"Slug of form whose response is getting submitted","required":true,"schema":{"type":"string"}}]}""", slug=slug)
        query_string = await create_query_string(slug=slug)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["submitCustomForm"]).netloc, "post", await create_url_without_domain("/service/application/lead/v1.0/form/{slug}/submit", slug=slug), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getParticipantsInsideVideoRoom(self, unique_name=None, body=""):
        """Get participants of a specific Video Room using it's unique name, this can be used to check if people are already there in the room and also to show their names.
        :param unique_name : Unique name of Video Room : type string
        """
        payload = {}
        
        if unique_name:
            payload["unique_name"] = unique_name
        
        # Parameter validation
        schema = LeadValidator.getParticipantsInsideVideoRoom()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getParticipantsInsideVideoRoom"], proccessed_params="""{"required":[{"name":"unique_name","in":"path","description":"Unique name of Video Room","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"unique_name","in":"path","description":"Unique name of Video Room","required":true,"schema":{"type":"string"}}]}""", unique_name=unique_name)
        query_string = await create_query_string(unique_name=unique_name)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getParticipantsInsideVideoRoom"]).netloc, "get", await create_url_without_domain("/service/application/lead/v1.0/video/room/{unique_name}/participants", unique_name=unique_name), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getTokenForVideoRoom(self, unique_name=None, body=""):
        """Get Token to join a specific Video Room using it's unqiue name, this Token is your ticket to Room and also creates your identity there.
        :param unique_name : Unique name of Video Room : type string
        """
        payload = {}
        
        if unique_name:
            payload["unique_name"] = unique_name
        
        # Parameter validation
        schema = LeadValidator.getTokenForVideoRoom()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getTokenForVideoRoom"], proccessed_params="""{"required":[{"name":"unique_name","in":"path","description":"Unique name of Video Room","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"unique_name","in":"path","description":"Unique name of Video Room","required":true,"schema":{"type":"string"}}]}""", unique_name=unique_name)
        query_string = await create_query_string(unique_name=unique_name)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getTokenForVideoRoom"]).netloc, "get", await create_url_without_domain("/service/application/lead/v1.0/video/room/{unique_name}/token", unique_name=unique_name), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    

class Theme:
    def __init__(self, config):
        self._conf = config
        self._relativeUrls = {
            "getAllPages": "/service/application/theme/v1.0/{theme_id}/page",
            "getPage": "/service/application/theme/v1.0/{theme_id}/{page_value}",
            "getAppliedTheme": "/service/application/theme/v1.0/applied-theme",
            "getThemeForPreview": "/service/application/theme/v1.0/{theme_id}/preview"
            
        }
        self._urls = {
            method: f"{self._conf.domain}{path}" for method, path in self._relativeUrls.items()
        }

    async def updateUrls(self, urls):
        self._urls.update(urls)
    
    async def getAllPages(self, theme_id=None, body=""):
        """Use this API to retrieve all the available pages of a theme by its ID.
        :param theme_id : ID of the theme to be retrieved : type string
        """
        payload = {}
        
        if theme_id:
            payload["theme_id"] = theme_id
        
        # Parameter validation
        schema = ThemeValidator.getAllPages()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getAllPages"], proccessed_params="""{"required":[{"name":"theme_id","in":"path","description":"ID of the theme to be retrieved","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"theme_id","in":"path","description":"ID of the theme to be retrieved","required":true,"schema":{"type":"string"}}]}""", theme_id=theme_id)
        query_string = await create_query_string(theme_id=theme_id)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getAllPages"]).netloc, "get", await create_url_without_domain("/service/application/theme/v1.0/{theme_id}/page", theme_id=theme_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getPage(self, theme_id=None, page_value=None, body=""):
        """Use this API to retrieve a page of a theme.
        :param theme_id : ID of the theme to be retrieved : type string
        :param page_value : Value of the page to be retrieved : type string
        """
        payload = {}
        
        if theme_id:
            payload["theme_id"] = theme_id
        
        if page_value:
            payload["page_value"] = page_value
        
        # Parameter validation
        schema = ThemeValidator.getPage()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getPage"], proccessed_params="""{"required":[{"name":"theme_id","in":"path","description":"ID of the theme to be retrieved","required":true,"schema":{"type":"string"}},{"name":"page_value","in":"path","description":"Value of the page to be retrieved","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"theme_id","in":"path","description":"ID of the theme to be retrieved","required":true,"schema":{"type":"string"}},{"name":"page_value","in":"path","description":"Value of the page to be retrieved","required":true,"schema":{"type":"string"}}]}""", theme_id=theme_id, page_value=page_value)
        query_string = await create_query_string(theme_id=theme_id, page_value=page_value)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getPage"]).netloc, "get", await create_url_without_domain("/service/application/theme/v1.0/{theme_id}/{page_value}", theme_id=theme_id, page_value=page_value), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getAppliedTheme(self, body=""):
        """An application has multiple themes, but only one theme can be applied at a time. Use this API to retrieve the theme currently applied to the application.
        """
        payload = {}
        
        # Parameter validation
        schema = ThemeValidator.getAppliedTheme()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getAppliedTheme"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getAppliedTheme"]).netloc, "get", await create_url_without_domain("/service/application/theme/v1.0/applied-theme", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getThemeForPreview(self, theme_id=None, body=""):
        """A theme can be previewed before applying it. Use this API to retrieve the preview of a theme by its ID.
        :param theme_id : ID of the theme to be retrieved : type string
        """
        payload = {}
        
        if theme_id:
            payload["theme_id"] = theme_id
        
        # Parameter validation
        schema = ThemeValidator.getThemeForPreview()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getThemeForPreview"], proccessed_params="""{"required":[{"name":"theme_id","in":"path","description":"ID of the theme to be retrieved","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"theme_id","in":"path","description":"ID of the theme to be retrieved","required":true,"schema":{"type":"string"}}]}""", theme_id=theme_id)
        query_string = await create_query_string(theme_id=theme_id)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getThemeForPreview"]).netloc, "get", await create_url_without_domain("/service/application/theme/v1.0/{theme_id}/preview", theme_id=theme_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    

class User:
    def __init__(self, config):
        self._conf = config
        self._relativeUrls = {
            "loginWithFacebook": "/service/application/user/authentication/v1.0/login/facebook-token",
            "loginWithGoogle": "/service/application/user/authentication/v1.0/login/google-token",
            "loginWithGoogleAndroid": "/service/application/user/authentication/v1.0/login/google-android",
            "loginWithGoogleIOS": "/service/application/user/authentication/v1.0/login/google-ios",
            "loginWithAppleIOS": "/service/application/user/authentication/v1.0/login/apple-ios",
            "loginWithOTP": "/service/application/user/authentication/v1.0/login/otp",
            "loginWithEmailAndPassword": "/service/application/user/authentication/v1.0/login/password",
            "sendResetPasswordEmail": "/service/application/user/authentication/v1.0/login/password/reset",
            "forgotPassword": "/service/application/user/authentication/v1.0/login/password/reset/forgot",
            "sendResetToken": "/service/application/user/authentication/v1.0/login/password/reset/token",
            "loginWithToken": "/service/application/user/authentication/v1.0/login/token",
            "registerWithForm": "/service/application/user/authentication/v1.0/register/form",
            "verifyEmail": "/service/application/user/authentication/v1.0/verify/email",
            "verifyMobile": "/service/application/user/authentication/v1.0/verify/mobile",
            "hasPassword": "/service/application/user/authentication/v1.0/has-password",
            "updatePassword": "/service/application/user/authentication/v1.0/password",
            "logout": "/service/application/user/authentication/v1.0/logout",
            "sendOTPOnMobile": "/service/application/user/authentication/v1.0/otp/mobile/send",
            "verifyMobileOTP": "/service/application/user/authentication/v1.0/otp/mobile/verify",
            "sendOTPOnEmail": "/service/application/user/authentication/v1.0/otp/email/send",
            "verifyEmailOTP": "/service/application/user/authentication/v1.0/otp/email/verify",
            "getLoggedInUser": "/service/application/user/authentication/v1.0/session",
            "getListOfActiveSessions": "/service/application/user/authentication/v1.0/sessions",
            "getPlatformConfig": "/service/application/user/platform/v1.0/config",
            "updateProfile": "/service/application/user/profile/v1.0/detail",
            "addMobileNumber": "/service/application/user/profile/v1.0/mobile",
            "deleteMobileNumber": "/service/application/user/profile/v1.0/mobile",
            "setMobileNumberAsPrimary": "/service/application/user/profile/v1.0/mobile/primary",
            "sendVerificationLinkToMobile": "/service/application/user/profile/v1.0/mobile/link/send",
            "addEmail": "/service/application/user/profile/v1.0/email",
            "deleteEmail": "/service/application/user/profile/v1.0/email",
            "setEmailAsPrimary": "/service/application/user/profile/v1.0/email/primary",
            "sendVerificationLinkToEmail": "/service/application/user/profile/v1.0/email/link/send"
            
        }
        self._urls = {
            method: f"{self._conf.domain}{path}" for method, path in self._relativeUrls.items()
        }

    async def updateUrls(self, urls):
        self._urls.update(urls)
    
    async def loginWithFacebook(self, platform=None, body=""):
        """Use this API to login or register using Facebook credentials.
        :param platform : ID of the application : type string
        """
        payload = {}
        
        if platform:
            payload["platform"] = platform
        
        # Parameter validation
        schema = UserValidator.loginWithFacebook()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.OAuthRequestSchema import OAuthRequestSchema
        schema = OAuthRequestSchema()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["loginWithFacebook"], proccessed_params="""{"required":[],"optional":[{"name":"platform","in":"query","description":"ID of the application","schema":{"type":"string","default":"Fynd"}}],"query":[{"name":"platform","in":"query","description":"ID of the application","schema":{"type":"string","default":"Fynd"}}],"headers":[],"path":[]}""", platform=platform)
        query_string = await create_query_string(platform=platform)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["loginWithFacebook"]).netloc, "post", await create_url_without_domain("/service/application/user/authentication/v1.0/login/facebook-token", platform=platform), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def loginWithGoogle(self, platform=None, body=""):
        """Use this API to login or register using Google Account credentials.
        :param platform : ID of the application : type string
        """
        payload = {}
        
        if platform:
            payload["platform"] = platform
        
        # Parameter validation
        schema = UserValidator.loginWithGoogle()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.OAuthRequestSchema import OAuthRequestSchema
        schema = OAuthRequestSchema()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["loginWithGoogle"], proccessed_params="""{"required":[],"optional":[{"name":"platform","in":"query","description":"ID of the application","schema":{"type":"string","default":"Fynd"}}],"query":[{"name":"platform","in":"query","description":"ID of the application","schema":{"type":"string","default":"Fynd"}}],"headers":[],"path":[]}""", platform=platform)
        query_string = await create_query_string(platform=platform)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["loginWithGoogle"]).netloc, "post", await create_url_without_domain("/service/application/user/authentication/v1.0/login/google-token", platform=platform), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def loginWithGoogleAndroid(self, platform=None, body=""):
        """Use this API to login or register in Android app using Google Account credentials.
        :param platform : ID of the application : type string
        """
        payload = {}
        
        if platform:
            payload["platform"] = platform
        
        # Parameter validation
        schema = UserValidator.loginWithGoogleAndroid()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.OAuthRequestSchema import OAuthRequestSchema
        schema = OAuthRequestSchema()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["loginWithGoogleAndroid"], proccessed_params="""{"required":[],"optional":[{"name":"platform","in":"query","description":"ID of the application","schema":{"type":"string","default":"Fynd"}}],"query":[{"name":"platform","in":"query","description":"ID of the application","schema":{"type":"string","default":"Fynd"}}],"headers":[],"path":[]}""", platform=platform)
        query_string = await create_query_string(platform=platform)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["loginWithGoogleAndroid"]).netloc, "post", await create_url_without_domain("/service/application/user/authentication/v1.0/login/google-android", platform=platform), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def loginWithGoogleIOS(self, platform=None, body=""):
        """Use this API to login or register in iOS app using Google Account credentials.
        :param platform : ID of the application : type string
        """
        payload = {}
        
        if platform:
            payload["platform"] = platform
        
        # Parameter validation
        schema = UserValidator.loginWithGoogleIOS()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.OAuthRequestSchema import OAuthRequestSchema
        schema = OAuthRequestSchema()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["loginWithGoogleIOS"], proccessed_params="""{"required":[],"optional":[{"name":"platform","in":"query","description":"ID of the application","schema":{"type":"string","default":"Fynd"}}],"query":[{"name":"platform","in":"query","description":"ID of the application","schema":{"type":"string","default":"Fynd"}}],"headers":[],"path":[]}""", platform=platform)
        query_string = await create_query_string(platform=platform)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["loginWithGoogleIOS"]).netloc, "post", await create_url_without_domain("/service/application/user/authentication/v1.0/login/google-ios", platform=platform), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def loginWithAppleIOS(self, platform=None, body=""):
        """Use this API to login or register in iOS app using Apple Account credentials.
        :param platform : ID of the application : type string
        """
        payload = {}
        
        if platform:
            payload["platform"] = platform
        
        # Parameter validation
        schema = UserValidator.loginWithAppleIOS()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.OAuthRequestAppleSchema import OAuthRequestAppleSchema
        schema = OAuthRequestAppleSchema()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["loginWithAppleIOS"], proccessed_params="""{"required":[],"optional":[{"name":"platform","in":"query","description":"ID of the application","schema":{"type":"string","default":"Fynd"}}],"query":[{"name":"platform","in":"query","description":"ID of the application","schema":{"type":"string","default":"Fynd"}}],"headers":[],"path":[]}""", platform=platform)
        query_string = await create_query_string(platform=platform)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["loginWithAppleIOS"]).netloc, "post", await create_url_without_domain("/service/application/user/authentication/v1.0/login/apple-ios", platform=platform), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def loginWithOTP(self, platform=None, body=""):
        """Use this API to login or register with a One-time Password (OTP) sent via Email or SMS.
        :param platform : ID of the application : type string
        """
        payload = {}
        
        if platform:
            payload["platform"] = platform
        
        # Parameter validation
        schema = UserValidator.loginWithOTP()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.SendOtpRequestSchema import SendOtpRequestSchema
        schema = SendOtpRequestSchema()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["loginWithOTP"], proccessed_params="""{"required":[],"optional":[{"name":"platform","in":"query","description":"ID of the application","schema":{"type":"string","default":"Fynd"}}],"query":[{"name":"platform","in":"query","description":"ID of the application","schema":{"type":"string","default":"Fynd"}}],"headers":[],"path":[]}""", platform=platform)
        query_string = await create_query_string(platform=platform)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["loginWithOTP"]).netloc, "post", await create_url_without_domain("/service/application/user/authentication/v1.0/login/otp", platform=platform), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def loginWithEmailAndPassword(self, body=""):
        """Use this API to login or register using an email address and password.
        """
        payload = {}
        
        # Parameter validation
        schema = UserValidator.loginWithEmailAndPassword()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.PasswordLoginRequestSchema import PasswordLoginRequestSchema
        schema = PasswordLoginRequestSchema()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["loginWithEmailAndPassword"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["loginWithEmailAndPassword"]).netloc, "post", await create_url_without_domain("/service/application/user/authentication/v1.0/login/password", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def sendResetPasswordEmail(self, platform=None, body=""):
        """Use this API to reset a password using the link sent on email.
        :param platform : ID of the application : type string
        """
        payload = {}
        
        if platform:
            payload["platform"] = platform
        
        # Parameter validation
        schema = UserValidator.sendResetPasswordEmail()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.SendResetPasswordEmailRequestSchema import SendResetPasswordEmailRequestSchema
        schema = SendResetPasswordEmailRequestSchema()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["sendResetPasswordEmail"], proccessed_params="""{"required":[],"optional":[{"name":"platform","in":"query","description":"ID of the application","schema":{"type":"string","default":"Fynd"}}],"query":[{"name":"platform","in":"query","description":"ID of the application","schema":{"type":"string","default":"Fynd"}}],"headers":[],"path":[]}""", platform=platform)
        query_string = await create_query_string(platform=platform)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["sendResetPasswordEmail"]).netloc, "post", await create_url_without_domain("/service/application/user/authentication/v1.0/login/password/reset", platform=platform), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def forgotPassword(self, body=""):
        """Use this API to reset a password using the code sent on email or SMS.
        """
        payload = {}
        
        # Parameter validation
        schema = UserValidator.forgotPassword()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.ForgotPasswordRequestSchema import ForgotPasswordRequestSchema
        schema = ForgotPasswordRequestSchema()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["forgotPassword"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["forgotPassword"]).netloc, "post", await create_url_without_domain("/service/application/user/authentication/v1.0/login/password/reset/forgot", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def sendResetToken(self, body=""):
        """Use this API to send code to reset password.
        """
        payload = {}
        
        # Parameter validation
        schema = UserValidator.sendResetToken()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.CodeRequestBodySchema import CodeRequestBodySchema
        schema = CodeRequestBodySchema()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["sendResetToken"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["sendResetToken"]).netloc, "post", await create_url_without_domain("/service/application/user/authentication/v1.0/login/password/reset/token", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def loginWithToken(self, body=""):
        """Use this API to login or register using a token for authentication.
        """
        payload = {}
        
        # Parameter validation
        schema = UserValidator.loginWithToken()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.TokenRequestBodySchema import TokenRequestBodySchema
        schema = TokenRequestBodySchema()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["loginWithToken"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["loginWithToken"]).netloc, "post", await create_url_without_domain("/service/application/user/authentication/v1.0/login/token", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def registerWithForm(self, platform=None, body=""):
        """Use this API to perform user registration by sending form data in the request body.
        :param platform : ID of the application : type string
        """
        payload = {}
        
        if platform:
            payload["platform"] = platform
        
        # Parameter validation
        schema = UserValidator.registerWithForm()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.FormRegisterRequestSchema import FormRegisterRequestSchema
        schema = FormRegisterRequestSchema()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["registerWithForm"], proccessed_params="""{"required":[],"optional":[{"name":"platform","in":"query","description":"ID of the application","schema":{"type":"string","default":"Fynd"}}],"query":[{"name":"platform","in":"query","description":"ID of the application","schema":{"type":"string","default":"Fynd"}}],"headers":[],"path":[]}""", platform=platform)
        query_string = await create_query_string(platform=platform)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["registerWithForm"]).netloc, "post", await create_url_without_domain("/service/application/user/authentication/v1.0/register/form", platform=platform), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def verifyEmail(self, body=""):
        """Use this API to send a verification code to verify an email.
        """
        payload = {}
        
        # Parameter validation
        schema = UserValidator.verifyEmail()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.CodeRequestBodySchema import CodeRequestBodySchema
        schema = CodeRequestBodySchema()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["verifyEmail"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["verifyEmail"]).netloc, "post", await create_url_without_domain("/service/application/user/authentication/v1.0/verify/email", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def verifyMobile(self, body=""):
        """Use this API to send a verification code to verify a mobile number.
        """
        payload = {}
        
        # Parameter validation
        schema = UserValidator.verifyMobile()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.CodeRequestBodySchema import CodeRequestBodySchema
        schema = CodeRequestBodySchema()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["verifyMobile"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["verifyMobile"]).netloc, "post", await create_url_without_domain("/service/application/user/authentication/v1.0/verify/mobile", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def hasPassword(self, body=""):
        """Use this API to check if user has created a password for login.
        """
        payload = {}
        
        # Parameter validation
        schema = UserValidator.hasPassword()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["hasPassword"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["hasPassword"]).netloc, "get", await create_url_without_domain("/service/application/user/authentication/v1.0/has-password", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def updatePassword(self, body=""):
        """Use this API to update the password.
        """
        payload = {}
        
        # Parameter validation
        schema = UserValidator.updatePassword()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.UpdatePasswordRequestSchema import UpdatePasswordRequestSchema
        schema = UpdatePasswordRequestSchema()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["updatePassword"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["updatePassword"]).netloc, "post", await create_url_without_domain("/service/application/user/authentication/v1.0/password", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def logout(self, body=""):
        """Use this API to check to logout a user from the app.
        """
        payload = {}
        
        # Parameter validation
        schema = UserValidator.logout()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["logout"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["logout"]).netloc, "get", await create_url_without_domain("/service/application/user/authentication/v1.0/logout", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def sendOTPOnMobile(self, platform=None, body=""):
        """Use this API to send an OTP to a mobile number.
        :param platform : ID of the application : type string
        """
        payload = {}
        
        if platform:
            payload["platform"] = platform
        
        # Parameter validation
        schema = UserValidator.sendOTPOnMobile()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.SendMobileOtpRequestSchema import SendMobileOtpRequestSchema
        schema = SendMobileOtpRequestSchema()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["sendOTPOnMobile"], proccessed_params="""{"required":[],"optional":[{"name":"platform","in":"query","description":"ID of the application","schema":{"type":"string","default":"Fynd"}}],"query":[{"name":"platform","in":"query","description":"ID of the application","schema":{"type":"string","default":"Fynd"}}],"headers":[],"path":[]}""", platform=platform)
        query_string = await create_query_string(platform=platform)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["sendOTPOnMobile"]).netloc, "post", await create_url_without_domain("/service/application/user/authentication/v1.0/otp/mobile/send", platform=platform), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def verifyMobileOTP(self, platform=None, body=""):
        """Use this API to verify the OTP received on a mobile number.
        :param platform : ID of the application : type string
        """
        payload = {}
        
        if platform:
            payload["platform"] = platform
        
        # Parameter validation
        schema = UserValidator.verifyMobileOTP()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.VerifyOtpRequestSchema import VerifyOtpRequestSchema
        schema = VerifyOtpRequestSchema()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["verifyMobileOTP"], proccessed_params="""{"required":[],"optional":[{"name":"platform","in":"query","description":"ID of the application","schema":{"type":"string","default":"Fynd"}}],"query":[{"name":"platform","in":"query","description":"ID of the application","schema":{"type":"string","default":"Fynd"}}],"headers":[],"path":[]}""", platform=platform)
        query_string = await create_query_string(platform=platform)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["verifyMobileOTP"]).netloc, "post", await create_url_without_domain("/service/application/user/authentication/v1.0/otp/mobile/verify", platform=platform), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def sendOTPOnEmail(self, platform=None, body=""):
        """Use this API to send an OTP to an email ID.
        :param platform : ID of the application : type string
        """
        payload = {}
        
        if platform:
            payload["platform"] = platform
        
        # Parameter validation
        schema = UserValidator.sendOTPOnEmail()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.SendEmailOtpRequestSchema import SendEmailOtpRequestSchema
        schema = SendEmailOtpRequestSchema()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["sendOTPOnEmail"], proccessed_params="""{"required":[],"optional":[{"name":"platform","in":"query","description":"ID of the application","schema":{"type":"string","default":"Fynd"}}],"query":[{"name":"platform","in":"query","description":"ID of the application","schema":{"type":"string","default":"Fynd"}}],"headers":[],"path":[]}""", platform=platform)
        query_string = await create_query_string(platform=platform)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["sendOTPOnEmail"]).netloc, "post", await create_url_without_domain("/service/application/user/authentication/v1.0/otp/email/send", platform=platform), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def verifyEmailOTP(self, platform=None, body=""):
        """Use this API to verify the OTP received on an email ID.
        :param platform : ID of the application : type string
        """
        payload = {}
        
        if platform:
            payload["platform"] = platform
        
        # Parameter validation
        schema = UserValidator.verifyEmailOTP()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.VerifyEmailOtpRequestSchema import VerifyEmailOtpRequestSchema
        schema = VerifyEmailOtpRequestSchema()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["verifyEmailOTP"], proccessed_params="""{"required":[],"optional":[{"name":"platform","in":"query","description":"ID of the application","schema":{"type":"string","default":"Fynd"}}],"query":[{"name":"platform","in":"query","description":"ID of the application","schema":{"type":"string","default":"Fynd"}}],"headers":[],"path":[]}""", platform=platform)
        query_string = await create_query_string(platform=platform)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["verifyEmailOTP"]).netloc, "post", await create_url_without_domain("/service/application/user/authentication/v1.0/otp/email/verify", platform=platform), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getLoggedInUser(self, body=""):
        """Use this API  to get the details of a logged in user.
        """
        payload = {}
        
        # Parameter validation
        schema = UserValidator.getLoggedInUser()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getLoggedInUser"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getLoggedInUser"]).netloc, "get", await create_url_without_domain("/service/application/user/authentication/v1.0/session", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getListOfActiveSessions(self, body=""):
        """Use this API to retrieve all active sessions of a user.
        """
        payload = {}
        
        # Parameter validation
        schema = UserValidator.getListOfActiveSessions()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getListOfActiveSessions"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getListOfActiveSessions"]).netloc, "get", await create_url_without_domain("/service/application/user/authentication/v1.0/sessions", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getPlatformConfig(self, name=None, body=""):
        """Use this API to get all the platform configurations such as mobile image, desktop image, social logins, and all other text.
        :param name : Name of the application, e.g. Fynd : type string
        """
        payload = {}
        
        if name:
            payload["name"] = name
        
        # Parameter validation
        schema = UserValidator.getPlatformConfig()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getPlatformConfig"], proccessed_params="""{"required":[],"optional":[{"name":"name","in":"query","description":"Name of the application, e.g. Fynd","schema":{"type":"string"}}],"query":[{"name":"name","in":"query","description":"Name of the application, e.g. Fynd","schema":{"type":"string"}}],"headers":[],"path":[]}""", name=name)
        query_string = await create_query_string(name=name)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getPlatformConfig"]).netloc, "get", await create_url_without_domain("/service/application/user/platform/v1.0/config", name=name), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def updateProfile(self, platform=None, body=""):
        """Use this API to update details in the user profile. Details can be first name, last name, gender, email, phone number, or profile picture.
        :param platform : ID of the application : type string
        """
        payload = {}
        
        if platform:
            payload["platform"] = platform
        
        # Parameter validation
        schema = UserValidator.updateProfile()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.EditProfileRequestSchema import EditProfileRequestSchema
        schema = EditProfileRequestSchema()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["updateProfile"], proccessed_params="""{"required":[],"optional":[{"name":"platform","in":"query","description":"ID of the application","schema":{"type":"string","default":"Fynd"}}],"query":[{"name":"platform","in":"query","description":"ID of the application","schema":{"type":"string","default":"Fynd"}}],"headers":[],"path":[]}""", platform=platform)
        query_string = await create_query_string(platform=platform)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["updateProfile"]).netloc, "post", await create_url_without_domain("/service/application/user/profile/v1.0/detail", platform=platform), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def addMobileNumber(self, platform=None, body=""):
        """Use this API to add a new mobile number to a profile.
        :param platform : ID of the application : type string
        """
        payload = {}
        
        if platform:
            payload["platform"] = platform
        
        # Parameter validation
        schema = UserValidator.addMobileNumber()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.EditMobileRequestSchema import EditMobileRequestSchema
        schema = EditMobileRequestSchema()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["addMobileNumber"], proccessed_params="""{"required":[],"optional":[{"name":"platform","in":"query","description":"ID of the application","schema":{"type":"string","default":"Fynd"}}],"query":[{"name":"platform","in":"query","description":"ID of the application","schema":{"type":"string","default":"Fynd"}}],"headers":[],"path":[]}""", platform=platform)
        query_string = await create_query_string(platform=platform)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["addMobileNumber"]).netloc, "put", await create_url_without_domain("/service/application/user/profile/v1.0/mobile", platform=platform), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def deleteMobileNumber(self, platform=None, active=None, primary=None, verified=None, country_code=None, phone=None, body=""):
        """Use this API to delete a mobile number from a profile.
        :param platform : ID of the application : type string
        :param active : This is a boolean value to check if mobile number is active 1.True - Number is active 2. False - Number is inactive : type boolean
        :param primary : This is a boolean value to check if mobile number is primary number (main number) 1. True - Number is primary 2. False - Number is not primary : type boolean
        :param verified : This is a boolean value to check if mobile number is verified 1. True - Number is verified 2.False - Number is not verified yet : type boolean
        :param country_code : Country code of the phone number, e.g. 91 : type string
        :param phone : Phone number : type string
        """
        payload = {}
        
        if platform:
            payload["platform"] = platform
        
        if active:
            payload["active"] = active
        
        if primary:
            payload["primary"] = primary
        
        if verified:
            payload["verified"] = verified
        
        if country_code:
            payload["country_code"] = country_code
        
        if phone:
            payload["phone"] = phone
        
        # Parameter validation
        schema = UserValidator.deleteMobileNumber()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["deleteMobileNumber"], proccessed_params="""{"required":[{"name":"active","in":"query","required":true,"description":"This is a boolean value to check if mobile number is active 1.True - Number is active 2. False - Number is inactive","schema":{"type":"boolean"}},{"name":"primary","in":"query","description":"This is a boolean value to check if mobile number is primary number (main number) 1. True - Number is primary 2. False - Number is not primary","required":true,"schema":{"type":"boolean"}},{"name":"verified","in":"query","description":"This is a boolean value to check if mobile number is verified 1. True - Number is verified 2.False - Number is not verified yet","required":true,"schema":{"type":"boolean"}},{"name":"country_code","in":"query","description":"Country code of the phone number, e.g. 91","required":true,"schema":{"type":"string"}},{"name":"phone","in":"query","description":"Phone number","required":true,"schema":{"type":"string"}}],"optional":[{"name":"platform","in":"query","description":"ID of the application","schema":{"type":"string","default":"Fynd"}}],"query":[{"name":"platform","in":"query","description":"ID of the application","schema":{"type":"string","default":"Fynd"}},{"name":"active","in":"query","required":true,"description":"This is a boolean value to check if mobile number is active 1.True - Number is active 2. False - Number is inactive","schema":{"type":"boolean"}},{"name":"primary","in":"query","description":"This is a boolean value to check if mobile number is primary number (main number) 1. True - Number is primary 2. False - Number is not primary","required":true,"schema":{"type":"boolean"}},{"name":"verified","in":"query","description":"This is a boolean value to check if mobile number is verified 1. True - Number is verified 2.False - Number is not verified yet","required":true,"schema":{"type":"boolean"}},{"name":"country_code","in":"query","description":"Country code of the phone number, e.g. 91","required":true,"schema":{"type":"string"}},{"name":"phone","in":"query","description":"Phone number","required":true,"schema":{"type":"string"}}],"headers":[],"path":[]}""", platform=platform, active=active, primary=primary, verified=verified, country_code=country_code, phone=phone)
        query_string = await create_query_string(platform=platform, active=active, primary=primary, verified=verified, country_code=country_code, phone=phone)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["deleteMobileNumber"]).netloc, "delete", await create_url_without_domain("/service/application/user/profile/v1.0/mobile", platform=platform, active=active, primary=primary, verified=verified, country_code=country_code, phone=phone), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def setMobileNumberAsPrimary(self, body=""):
        """Use this API to set a mobile number as primary. Primary number is a verified number used for all future communications.
        """
        payload = {}
        
        # Parameter validation
        schema = UserValidator.setMobileNumberAsPrimary()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.SendVerificationLinkMobileRequestSchema import SendVerificationLinkMobileRequestSchema
        schema = SendVerificationLinkMobileRequestSchema()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["setMobileNumberAsPrimary"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["setMobileNumberAsPrimary"]).netloc, "post", await create_url_without_domain("/service/application/user/profile/v1.0/mobile/primary", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def sendVerificationLinkToMobile(self, platform=None, body=""):
        """Use this API to send a verification link to a mobile number
        :param platform : ID of the application : type string
        """
        payload = {}
        
        if platform:
            payload["platform"] = platform
        
        # Parameter validation
        schema = UserValidator.sendVerificationLinkToMobile()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.SendVerificationLinkMobileRequestSchema import SendVerificationLinkMobileRequestSchema
        schema = SendVerificationLinkMobileRequestSchema()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["sendVerificationLinkToMobile"], proccessed_params="""{"required":[],"optional":[{"name":"platform","in":"query","description":"ID of the application","schema":{"type":"string","default":"Fynd"}}],"query":[{"name":"platform","in":"query","description":"ID of the application","schema":{"type":"string","default":"Fynd"}}],"headers":[],"path":[]}""", platform=platform)
        query_string = await create_query_string(platform=platform)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["sendVerificationLinkToMobile"]).netloc, "post", await create_url_without_domain("/service/application/user/profile/v1.0/mobile/link/send", platform=platform), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def addEmail(self, platform=None, body=""):
        """Use this API to add a new email address to a profile
        :param platform : ID of the application : type string
        """
        payload = {}
        
        if platform:
            payload["platform"] = platform
        
        # Parameter validation
        schema = UserValidator.addEmail()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.EditEmailRequestSchema import EditEmailRequestSchema
        schema = EditEmailRequestSchema()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["addEmail"], proccessed_params="""{"required":[],"optional":[{"name":"platform","in":"query","description":"ID of the application","schema":{"type":"string","default":"Fynd"}}],"query":[{"name":"platform","in":"query","description":"ID of the application","schema":{"type":"string","default":"Fynd"}}],"headers":[],"path":[]}""", platform=platform)
        query_string = await create_query_string(platform=platform)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["addEmail"]).netloc, "put", await create_url_without_domain("/service/application/user/profile/v1.0/email", platform=platform), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def deleteEmail(self, platform=None, active=None, primary=None, verified=None, email=None, body=""):
        """Use this API to delete an email address from a profile
        :param platform : ID of the application : type string
        :param active : This is a boolean value to check if email ID is active 1. True - Email ID is active 2.False - Email ID is inactive : type boolean
        :param primary : This is a boolean value to check if email ID is primary (main email ID) 1. True - Email ID is primary 2.False - Email ID is not primary : type boolean
        :param verified : This is a boolean value to check if email ID is verified 1. True - Email ID is verified 2.False - Email ID is not verified yet : type boolean
        :param email : The email ID to delete : type string
        """
        payload = {}
        
        if platform:
            payload["platform"] = platform
        
        if active:
            payload["active"] = active
        
        if primary:
            payload["primary"] = primary
        
        if verified:
            payload["verified"] = verified
        
        if email:
            payload["email"] = email
        
        # Parameter validation
        schema = UserValidator.deleteEmail()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["deleteEmail"], proccessed_params="""{"required":[{"name":"active","in":"query","description":"This is a boolean value to check if email ID is active 1. True - Email ID is active 2.False - Email ID is inactive","required":true,"schema":{"type":"boolean"}},{"name":"primary","in":"query","description":"This is a boolean value to check if email ID is primary (main email ID) 1. True - Email ID is primary 2.False - Email ID is not primary","required":true,"schema":{"type":"boolean"}},{"name":"verified","in":"query","description":"This is a boolean value to check if email ID is verified 1. True - Email ID is verified 2.False - Email ID is not verified yet","required":true,"schema":{"type":"boolean"}},{"name":"email","in":"query","description":"The email ID to delete","required":true,"schema":{"type":"string"}}],"optional":[{"name":"platform","in":"query","description":"ID of the application","schema":{"type":"string","default":"Fynd"}}],"query":[{"name":"platform","in":"query","description":"ID of the application","schema":{"type":"string","default":"Fynd"}},{"name":"active","in":"query","description":"This is a boolean value to check if email ID is active 1. True - Email ID is active 2.False - Email ID is inactive","required":true,"schema":{"type":"boolean"}},{"name":"primary","in":"query","description":"This is a boolean value to check if email ID is primary (main email ID) 1. True - Email ID is primary 2.False - Email ID is not primary","required":true,"schema":{"type":"boolean"}},{"name":"verified","in":"query","description":"This is a boolean value to check if email ID is verified 1. True - Email ID is verified 2.False - Email ID is not verified yet","required":true,"schema":{"type":"boolean"}},{"name":"email","in":"query","description":"The email ID to delete","required":true,"schema":{"type":"string"}}],"headers":[],"path":[]}""", platform=platform, active=active, primary=primary, verified=verified, email=email)
        query_string = await create_query_string(platform=platform, active=active, primary=primary, verified=verified, email=email)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["deleteEmail"]).netloc, "delete", await create_url_without_domain("/service/application/user/profile/v1.0/email", platform=platform, active=active, primary=primary, verified=verified, email=email), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def setEmailAsPrimary(self, body=""):
        """Use this API to set an email address as primary. Primary email ID is a email address used for all future communications.
        """
        payload = {}
        
        # Parameter validation
        schema = UserValidator.setEmailAsPrimary()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.EditEmailRequestSchema import EditEmailRequestSchema
        schema = EditEmailRequestSchema()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["setEmailAsPrimary"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["setEmailAsPrimary"]).netloc, "post", await create_url_without_domain("/service/application/user/profile/v1.0/email/primary", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def sendVerificationLinkToEmail(self, platform=None, body=""):
        """Use this API to send verification link to an email address.
        :param platform : ID of the application : type string
        """
        payload = {}
        
        if platform:
            payload["platform"] = platform
        
        # Parameter validation
        schema = UserValidator.sendVerificationLinkToEmail()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.EditEmailRequestSchema import EditEmailRequestSchema
        schema = EditEmailRequestSchema()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["sendVerificationLinkToEmail"], proccessed_params="""{"required":[],"optional":[{"name":"platform","in":"query","description":"ID of the application","schema":{"type":"string","default":"Fynd"}}],"query":[{"name":"platform","in":"query","description":"ID of the application","schema":{"type":"string","default":"Fynd"}}],"headers":[],"path":[]}""", platform=platform)
        query_string = await create_query_string(platform=platform)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["sendVerificationLinkToEmail"]).netloc, "post", await create_url_without_domain("/service/application/user/profile/v1.0/email/link/send", platform=platform), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    

class Content:
    def __init__(self, config):
        self._conf = config
        self._relativeUrls = {
            "getAnnouncements": "/service/application/content/v1.0/announcements",
            "getBlog": "/service/application/content/v1.0/blogs/{slug}",
            "getBlogs": "/service/application/content/v1.0/blogs/",
            "getDataLoaders": "/service/application/content/v1.0/data-loader",
            "getFaqs": "/service/application/content/v1.0/faq",
            "getFaqCategories": "/service/application/content/v1.0/faq/categories",
            "getFaqBySlug": "/service/application/content/v1.0/faq/{slug}",
            "getFaqCategoryBySlug": "/service/application/content/v1.0/faq/category/{slug}",
            "getFaqsByCategorySlug": "/service/application/content/v1.0/faq/category/{slug}/faqs",
            "getLandingPage": "/service/application/content/v1.0/landing-page",
            "getLegalInformation": "/service/application/content/v1.0/legal",
            "getNavigations": "/service/application/content/v1.0/navigations/",
            "getSEOConfiguration": "/service/application/content/v1.0/seo",
            "getSlideshows": "/service/application/content/v1.0/slideshow/",
            "getSlideshow": "/service/application/content/v1.0/slideshow/{slug}",
            "getSupportInformation": "/service/application/content/v1.0/support",
            "getTags": "/service/application/content/v1.0/tags",
            "getPage": "/service/application/content/v2.0/pages/{slug}",
            "getPages": "/service/application/content/v2.0/pages/"
            
        }
        self._urls = {
            method: f"{self._conf.domain}{path}" for method, path in self._relativeUrls.items()
        }

    async def updateUrls(self, urls):
        self._urls.update(urls)
    
    async def getAnnouncements(self, body=""):
        """Announcements are useful to highlight a message or information on top of a webpage. Use this API to retrieve live announcements. Get announcements on individual pages or for all pages.
        """
        payload = {}
        
        # Parameter validation
        schema = ContentValidator.getAnnouncements()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getAnnouncements"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getAnnouncements"]).netloc, "get", await create_url_without_domain("/service/application/content/v1.0/announcements", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getBlog(self, slug=None, root_id=None, body=""):
        """Use this API to get the details of a blog using its slug. Details include the title, reading time, publish status, feature image, tags, author, etc.
        :param slug : A short, human-readable, URL-friendly identifier of a blog. You can get slug value from the endpoint /service/application/content/v1.0/blogs/. : type string
        :param root_id : ID given to the HTML element : type string
        """
        payload = {}
        
        if slug:
            payload["slug"] = slug
        
        if root_id:
            payload["root_id"] = root_id
        
        # Parameter validation
        schema = ContentValidator.getBlog()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getBlog"], proccessed_params="""{"required":[{"name":"slug","in":"path","description":"A short, human-readable, URL-friendly identifier of a blog. You can get slug value from the endpoint /service/application/content/v1.0/blogs/.","required":true,"schema":{"type":"string"}}],"optional":[{"name":"root_id","in":"query","description":"ID given to the HTML element","required":false,"schema":{"type":"string"}}],"query":[{"name":"root_id","in":"query","description":"ID given to the HTML element","required":false,"schema":{"type":"string"}}],"headers":[],"path":[{"name":"slug","in":"path","description":"A short, human-readable, URL-friendly identifier of a blog. You can get slug value from the endpoint /service/application/content/v1.0/blogs/.","required":true,"schema":{"type":"string"}}]}""", slug=slug, root_id=root_id)
        query_string = await create_query_string(slug=slug, root_id=root_id)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getBlog"]).netloc, "get", await create_url_without_domain("/service/application/content/v1.0/blogs/{slug}", slug=slug, root_id=root_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getBlogs(self, page_no=None, page_size=None, body=""):
        """Use this API to get all the blogs.
        :param page_no : The page number to navigate through the given set of results. Default value is 1.  : type integer
        :param page_size : The number of items to retrieve in each page. : type integer
        """
        payload = {}
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        
        # Parameter validation
        schema = ContentValidator.getBlogs()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getBlogs"], proccessed_params="""{"required":[],"optional":[{"name":"page_no","in":"query","description":"The page number to navigate through the given set of results. Default value is 1. ","required":false,"schema":{"type":"integer","default":1}},{"name":"page_size","in":"query","description":"The number of items to retrieve in each page.","required":false,"schema":{"type":"integer","default":10}}],"query":[{"name":"page_no","in":"query","description":"The page number to navigate through the given set of results. Default value is 1. ","required":false,"schema":{"type":"integer","default":1}},{"name":"page_size","in":"query","description":"The number of items to retrieve in each page.","required":false,"schema":{"type":"integer","default":10}}],"headers":[],"path":[]}""", page_no=page_no, page_size=page_size)
        query_string = await create_query_string(page_no=page_no, page_size=page_size)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getBlogs"]).netloc, "get", await create_url_without_domain("/service/application/content/v1.0/blogs/", page_no=page_no, page_size=page_size), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getDataLoaders(self, body=""):
        """Use this API to get all selected data loaders of the application in the form of tags.
        """
        payload = {}
        
        # Parameter validation
        schema = ContentValidator.getDataLoaders()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getDataLoaders"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getDataLoaders"]).netloc, "get", await create_url_without_domain("/service/application/content/v1.0/data-loader", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getFaqs(self, body=""):
        """Use this API to get a list of frequently asked questions. Users will benefit from it when facing any issue with the website.
        """
        payload = {}
        
        # Parameter validation
        schema = ContentValidator.getFaqs()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getFaqs"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getFaqs"]).netloc, "get", await create_url_without_domain("/service/application/content/v1.0/faq", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getFaqCategories(self, body=""):
        """FAQs can be divided into categories. Use this API to get a list of FAQ categories.
        """
        payload = {}
        
        # Parameter validation
        schema = ContentValidator.getFaqCategories()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getFaqCategories"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getFaqCategories"]).netloc, "get", await create_url_without_domain("/service/application/content/v1.0/faq/categories", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getFaqBySlug(self, slug=None, body=""):
        """Use this API to get a particular FAQ by its slug.
        :param slug : A short, human-readable, URL-friendly identifier of an FAQ. You can get slug value from the endpoint /service/application/content/v1.0/faq. : type string
        """
        payload = {}
        
        if slug:
            payload["slug"] = slug
        
        # Parameter validation
        schema = ContentValidator.getFaqBySlug()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getFaqBySlug"], proccessed_params="""{"required":[{"name":"slug","in":"path","description":"A short, human-readable, URL-friendly identifier of an FAQ. You can get slug value from the endpoint /service/application/content/v1.0/faq.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"slug","in":"path","description":"A short, human-readable, URL-friendly identifier of an FAQ. You can get slug value from the endpoint /service/application/content/v1.0/faq.","required":true,"schema":{"type":"string"}}]}""", slug=slug)
        query_string = await create_query_string(slug=slug)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getFaqBySlug"]).netloc, "get", await create_url_without_domain("/service/application/content/v1.0/faq/{slug}", slug=slug), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getFaqCategoryBySlug(self, slug=None, body=""):
        """FAQs can be divided into categories. Use this API to get the category to which an FAQ belongs.
        :param slug : A short, human-readable, URL-friendly identifier of an FAQ category. You can get slug value from the endpoint /service/application/content/v1.0/faq/categories. : type string
        """
        payload = {}
        
        if slug:
            payload["slug"] = slug
        
        # Parameter validation
        schema = ContentValidator.getFaqCategoryBySlug()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getFaqCategoryBySlug"], proccessed_params="""{"required":[{"name":"slug","in":"path","description":"A short, human-readable, URL-friendly identifier of an FAQ category. You can get slug value from the endpoint /service/application/content/v1.0/faq/categories.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"slug","in":"path","description":"A short, human-readable, URL-friendly identifier of an FAQ category. You can get slug value from the endpoint /service/application/content/v1.0/faq/categories.","required":true,"schema":{"type":"string"}}]}""", slug=slug)
        query_string = await create_query_string(slug=slug)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getFaqCategoryBySlug"]).netloc, "get", await create_url_without_domain("/service/application/content/v1.0/faq/category/{slug}", slug=slug), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getFaqsByCategorySlug(self, slug=None, body=""):
        """FAQs can be divided into categories. Use this API to get all the FAQs belonging to a category by using the category slug.
        :param slug : A short, human-readable, URL-friendly identifier of an FAQ category. You can get slug value from the endpoint /service/application/content/v1.0/faq/categories. : type string
        """
        payload = {}
        
        if slug:
            payload["slug"] = slug
        
        # Parameter validation
        schema = ContentValidator.getFaqsByCategorySlug()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getFaqsByCategorySlug"], proccessed_params="""{"required":[{"name":"slug","in":"path","description":"A short, human-readable, URL-friendly identifier of an FAQ category. You can get slug value from the endpoint /service/application/content/v1.0/faq/categories.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"slug","in":"path","description":"A short, human-readable, URL-friendly identifier of an FAQ category. You can get slug value from the endpoint /service/application/content/v1.0/faq/categories.","required":true,"schema":{"type":"string"}}]}""", slug=slug)
        query_string = await create_query_string(slug=slug)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getFaqsByCategorySlug"]).netloc, "get", await create_url_without_domain("/service/application/content/v1.0/faq/category/{slug}/faqs", slug=slug), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getLandingPage(self, body=""):
        """Landing page is the first page that a prospect lands upon while visiting a website. Use this API to fetch the details of a landing page.
        """
        payload = {}
        
        # Parameter validation
        schema = ContentValidator.getLandingPage()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getLandingPage"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getLandingPage"]).netloc, "get", await create_url_without_domain("/service/application/content/v1.0/landing-page", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getLegalInformation(self, body=""):
        """Use this API to get the legal information of an application, which includes Privacy Policy, Terms and Conditions, Shipping Policy and FAQs regarding the usage of the application.
        """
        payload = {}
        
        # Parameter validation
        schema = ContentValidator.getLegalInformation()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getLegalInformation"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getLegalInformation"]).netloc, "get", await create_url_without_domain("/service/application/content/v1.0/legal", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getNavigations(self, page_no=None, page_size=None, body=""):
        """Use this API to fetch the navigations details which includes the items of the navigation pane. It also shows the links and sub-navigations.
        :param page_no : The page number to navigate through the given set of results. Default value is 1.  : type integer
        :param page_size : The number of items to retrieve in each page. : type integer
        """
        payload = {}
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        
        # Parameter validation
        schema = ContentValidator.getNavigations()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getNavigations"], proccessed_params="""{"required":[],"optional":[{"name":"page_no","in":"query","description":"The page number to navigate through the given set of results. Default value is 1. ","required":false,"schema":{"type":"integer","default":1}},{"name":"page_size","in":"query","description":"The number of items to retrieve in each page.","required":false,"schema":{"type":"integer","default":10}}],"query":[{"name":"page_no","in":"query","description":"The page number to navigate through the given set of results. Default value is 1. ","required":false,"schema":{"type":"integer","default":1}},{"name":"page_size","in":"query","description":"The number of items to retrieve in each page.","required":false,"schema":{"type":"integer","default":10}}],"headers":[],"path":[]}""", page_no=page_no, page_size=page_size)
        query_string = await create_query_string(page_no=page_no, page_size=page_size)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getNavigations"]).netloc, "get", await create_url_without_domain("/service/application/content/v1.0/navigations/", page_no=page_no, page_size=page_size), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getSEOConfiguration(self, body=""):
        """Use this API to get the SEO details of an application, which includes a robot.txt, meta-tags and sitemap.
        """
        payload = {}
        
        # Parameter validation
        schema = ContentValidator.getSEOConfiguration()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getSEOConfiguration"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getSEOConfiguration"]).netloc, "get", await create_url_without_domain("/service/application/content/v1.0/seo", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getSlideshows(self, page_no=None, page_size=None, body=""):
        """Use this API to get a list of slideshows along with their details.
        :param page_no : The page number to navigate through the given set of results. Default value is 1.  : type integer
        :param page_size : The number of items to retrieve in each page. : type integer
        """
        payload = {}
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        
        # Parameter validation
        schema = ContentValidator.getSlideshows()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getSlideshows"], proccessed_params="""{"required":[],"optional":[{"name":"page_no","in":"query","description":"The page number to navigate through the given set of results. Default value is 1. ","required":false,"schema":{"type":"integer","default":1}},{"name":"page_size","in":"query","description":"The number of items to retrieve in each page.","required":false,"schema":{"type":"integer","default":10}}],"query":[{"name":"page_no","in":"query","description":"The page number to navigate through the given set of results. Default value is 1. ","required":false,"schema":{"type":"integer","default":1}},{"name":"page_size","in":"query","description":"The number of items to retrieve in each page.","required":false,"schema":{"type":"integer","default":10}}],"headers":[],"path":[]}""", page_no=page_no, page_size=page_size)
        query_string = await create_query_string(page_no=page_no, page_size=page_size)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getSlideshows"]).netloc, "get", await create_url_without_domain("/service/application/content/v1.0/slideshow/", page_no=page_no, page_size=page_size), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getSlideshow(self, slug=None, body=""):
        """A slideshow is a group of images, videos or a combination of both that are shown on the website in the form of slides. Use this API to fetch a slideshow using its `slug`.
        :param slug : A short, human-readable, URL-friendly identifier of a slideshow. You can get slug value from the endpoint /service/application/content/v1.0/slideshow/. : type string
        """
        payload = {}
        
        if slug:
            payload["slug"] = slug
        
        # Parameter validation
        schema = ContentValidator.getSlideshow()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getSlideshow"], proccessed_params="""{"required":[{"name":"slug","in":"path","description":"A short, human-readable, URL-friendly identifier of a slideshow. You can get slug value from the endpoint /service/application/content/v1.0/slideshow/.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"slug","in":"path","description":"A short, human-readable, URL-friendly identifier of a slideshow. You can get slug value from the endpoint /service/application/content/v1.0/slideshow/.","required":true,"schema":{"type":"string"}}]}""", slug=slug)
        query_string = await create_query_string(slug=slug)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getSlideshow"]).netloc, "get", await create_url_without_domain("/service/application/content/v1.0/slideshow/{slug}", slug=slug), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getSupportInformation(self, body=""):
        """Use this API to get contact details for customer support including emails and phone numbers.
        """
        payload = {}
        
        # Parameter validation
        schema = ContentValidator.getSupportInformation()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getSupportInformation"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getSupportInformation"]).netloc, "get", await create_url_without_domain("/service/application/content/v1.0/support", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getTags(self, body=""):
        """Use this API to get all the CSS and JS injected in the application in the form of tags.
        """
        payload = {}
        
        # Parameter validation
        schema = ContentValidator.getTags()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getTags"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getTags"]).netloc, "get", await create_url_without_domain("/service/application/content/v1.0/tags", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getPage(self, slug=None, root_id=None, body=""):
        """Use this API to get the details of a page using its slug. Details include the title, seo, publish status, feature image, tags, meta, etc.
        :param slug : A short, human-readable, URL-friendly identifier of a page. You can get slug value from the endpoint /service/application/content/v2.0/pages/. : type string
        :param root_id : ID given to the HTML element : type string
        """
        payload = {}
        
        if slug:
            payload["slug"] = slug
        
        if root_id:
            payload["root_id"] = root_id
        
        # Parameter validation
        schema = ContentValidator.getPage()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getPage"], proccessed_params="""{"required":[{"name":"slug","in":"path","description":"A short, human-readable, URL-friendly identifier of a page. You can get slug value from the endpoint /service/application/content/v2.0/pages/.","required":true,"schema":{"type":"string"}}],"optional":[{"name":"root_id","in":"query","description":"ID given to the HTML element","required":false,"schema":{"type":"string"}}],"query":[{"name":"root_id","in":"query","description":"ID given to the HTML element","required":false,"schema":{"type":"string"}}],"headers":[],"path":[{"name":"slug","in":"path","description":"A short, human-readable, URL-friendly identifier of a page. You can get slug value from the endpoint /service/application/content/v2.0/pages/.","required":true,"schema":{"type":"string"}}]}""", slug=slug, root_id=root_id)
        query_string = await create_query_string(slug=slug, root_id=root_id)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getPage"]).netloc, "get", await create_url_without_domain("/service/application/content/v2.0/pages/{slug}", slug=slug, root_id=root_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getPages(self, page_no=None, page_size=None, body=""):
        """Use this API to get a list of pages.
        :param page_no : The page number to navigate through the given set of results. Default value is 1.  : type integer
        :param page_size : The number of items to retrieve in each page. : type integer
        """
        payload = {}
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        
        # Parameter validation
        schema = ContentValidator.getPages()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getPages"], proccessed_params="""{"required":[],"optional":[{"name":"page_no","in":"query","description":"The page number to navigate through the given set of results. Default value is 1. ","required":false,"schema":{"type":"integer","default":1}},{"name":"page_size","in":"query","description":"The number of items to retrieve in each page.","required":false,"schema":{"type":"integer","default":10}}],"query":[{"name":"page_no","in":"query","description":"The page number to navigate through the given set of results. Default value is 1. ","required":false,"schema":{"type":"integer","default":1}},{"name":"page_size","in":"query","description":"The number of items to retrieve in each page.","required":false,"schema":{"type":"integer","default":10}}],"headers":[],"path":[]}""", page_no=page_no, page_size=page_size)
        query_string = await create_query_string(page_no=page_no, page_size=page_size)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getPages"]).netloc, "get", await create_url_without_domain("/service/application/content/v2.0/pages/", page_no=page_no, page_size=page_size), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    

class Communication:
    def __init__(self, config):
        self._conf = config
        self._relativeUrls = {
            "getCommunicationConsent": "/service/application/communication/v1.0/consent",
            "upsertCommunicationConsent": "/service/application/communication/v1.0/consent",
            "upsertAppPushtoken": "/service/application/communication/v1.0/pn-token"
            
        }
        self._urls = {
            method: f"{self._conf.domain}{path}" for method, path in self._relativeUrls.items()
        }

    async def updateUrls(self, urls):
        self._urls.update(urls)
    
    async def getCommunicationConsent(self, body=""):
        """Use this API to retrieve the consent provided by the user for receiving communication messages over Email/SMS/WhatsApp.
        """
        payload = {}
        
        # Parameter validation
        schema = CommunicationValidator.getCommunicationConsent()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getCommunicationConsent"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getCommunicationConsent"]).netloc, "get", await create_url_without_domain("/service/application/communication/v1.0/consent", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def upsertCommunicationConsent(self, body=""):
        """Use this API to update and insert the consent provided by the user for receiving communication messages over Email/SMS/WhatsApp.
        """
        payload = {}
        
        # Parameter validation
        schema = CommunicationValidator.upsertCommunicationConsent()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.CommunicationConsentReq import CommunicationConsentReq
        schema = CommunicationConsentReq()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["upsertCommunicationConsent"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["upsertCommunicationConsent"]).netloc, "post", await create_url_without_domain("/service/application/communication/v1.0/consent", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def upsertAppPushtoken(self, body=""):
        """Use this API to update and insert the push token of the user.
        """
        payload = {}
        
        # Parameter validation
        schema = CommunicationValidator.upsertAppPushtoken()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.PushtokenReq import PushtokenReq
        schema = PushtokenReq()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["upsertAppPushtoken"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["upsertAppPushtoken"]).netloc, "post", await create_url_without_domain("/service/application/communication/v1.0/pn-token", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    

class Share:
    def __init__(self, config):
        self._conf = config
        self._relativeUrls = {
            "getApplicationQRCode": "/service/application/share/v1.0/qr/",
            "getProductQRCodeBySlug": "/service/application/share/v1.0/qr/products/{slug}/",
            "getCollectionQRCodeBySlug": "/service/application/share/v1.0/qr/collection/{slug}/",
            "getUrlQRCode": "/service/application/share/v1.0/qr/url/",
            "createShortLink": "/service/application/share/v1.0/links/short-link/",
            "getShortLinkByHash": "/service/application/share/v1.0/links/short-link/{hash}/",
            "getOriginalShortLinkByHash": "/service/application/share/v1.0/links/short-link/{hash}/original/"
            
        }
        self._urls = {
            method: f"{self._conf.domain}{path}" for method, path in self._relativeUrls.items()
        }

    async def updateUrls(self, urls):
        self._urls.update(urls)
    
    async def getApplicationQRCode(self, body=""):
        """Use this API to create a QR code of an app for sharing it with users who want to use the app.
        """
        payload = {}
        
        # Parameter validation
        schema = ShareValidator.getApplicationQRCode()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getApplicationQRCode"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getApplicationQRCode"]).netloc, "post", await create_url_without_domain("/service/application/share/v1.0/qr/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getProductQRCodeBySlug(self, slug=None, body=""):
        """Use this API to create a QR code of a product for sharing it with users who want to view/purchase the product.
        :param slug : A short, human-readable, URL-friendly identifier of a product. You can get slug value from the endpoint. : type string
        """
        payload = {}
        
        if slug:
            payload["slug"] = slug
        
        # Parameter validation
        schema = ShareValidator.getProductQRCodeBySlug()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getProductQRCodeBySlug"], proccessed_params="""{"required":[{"name":"slug","in":"path","description":"A short, human-readable, URL-friendly identifier of a product. You can get slug value from the endpoint.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"slug","in":"path","description":"A short, human-readable, URL-friendly identifier of a product. You can get slug value from the endpoint.","required":true,"schema":{"type":"string"}}]}""", slug=slug)
        query_string = await create_query_string(slug=slug)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getProductQRCodeBySlug"]).netloc, "post", await create_url_without_domain("/service/application/share/v1.0/qr/products/{slug}/", slug=slug), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getCollectionQRCodeBySlug(self, slug=None, body=""):
        """Use this API to create a QR code of a collection of products for sharing it with users who want to view/purchase the collection.
        :param slug : A short, human-readable, URL-friendly identifier of a collection. You can get slug value from the endpoint. : type string
        """
        payload = {}
        
        if slug:
            payload["slug"] = slug
        
        # Parameter validation
        schema = ShareValidator.getCollectionQRCodeBySlug()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getCollectionQRCodeBySlug"], proccessed_params="""{"required":[{"name":"slug","in":"path","description":"A short, human-readable, URL-friendly identifier of a collection. You can get slug value from the endpoint.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"slug","in":"path","description":"A short, human-readable, URL-friendly identifier of a collection. You can get slug value from the endpoint.","required":true,"schema":{"type":"string"}}]}""", slug=slug)
        query_string = await create_query_string(slug=slug)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getCollectionQRCodeBySlug"]).netloc, "post", await create_url_without_domain("/service/application/share/v1.0/qr/collection/{slug}/", slug=slug), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getUrlQRCode(self, url=None, body=""):
        """Use this API to create a QR code of a URL for sharing it with users who want to visit the link.
        :param url : A link or a web address : type string
        """
        payload = {}
        
        if url:
            payload["url"] = url
        
        # Parameter validation
        schema = ShareValidator.getUrlQRCode()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getUrlQRCode"], proccessed_params="""{"required":[{"name":"url","in":"query","description":"A link or a web address","required":true,"schema":{"type":"string"}}],"optional":[],"query":[{"name":"url","in":"query","description":"A link or a web address","required":true,"schema":{"type":"string"}}],"headers":[],"path":[]}""", url=url)
        query_string = await create_query_string(url=url)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getUrlQRCode"]).netloc, "post", await create_url_without_domain("/service/application/share/v1.0/qr/url/", url=url), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def createShortLink(self, body=""):
        """Use this API to create a short link that is easy to write/share/read as compared to long URLs.
        """
        payload = {}
        
        # Parameter validation
        schema = ShareValidator.createShortLink()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.ShortLinkReq import ShortLinkReq
        schema = ShortLinkReq()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["createShortLink"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["createShortLink"]).netloc, "post", await create_url_without_domain("/service/application/share/v1.0/links/short-link/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getShortLinkByHash(self, hash=None, body=""):
        """Use this API to get a short link by using a hash value.
        :param hash : A string value used for converting long URL to short URL and vice-versa. : type string
        """
        payload = {}
        
        if hash:
            payload["hash"] = hash
        
        # Parameter validation
        schema = ShareValidator.getShortLinkByHash()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getShortLinkByHash"], proccessed_params="""{"required":[{"name":"hash","in":"path","description":"A string value used for converting long URL to short URL and vice-versa.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"hash","in":"path","description":"A string value used for converting long URL to short URL and vice-versa.","required":true,"schema":{"type":"string"}}]}""", hash=hash)
        query_string = await create_query_string(hash=hash)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getShortLinkByHash"]).netloc, "get", await create_url_without_domain("/service/application/share/v1.0/links/short-link/{hash}/", hash=hash), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getOriginalShortLinkByHash(self, hash=None, body=""):
        """Use this API to retrieve the original link from a short-link by using a hash value.
        :param hash : A string value used for converting long URL to short URL and vice-versa. : type string
        """
        payload = {}
        
        if hash:
            payload["hash"] = hash
        
        # Parameter validation
        schema = ShareValidator.getOriginalShortLinkByHash()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getOriginalShortLinkByHash"], proccessed_params="""{"required":[{"name":"hash","in":"path","description":"A string value used for converting long URL to short URL and vice-versa.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"hash","in":"path","description":"A string value used for converting long URL to short URL and vice-versa.","required":true,"schema":{"type":"string"}}]}""", hash=hash)
        query_string = await create_query_string(hash=hash)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getOriginalShortLinkByHash"]).netloc, "get", await create_url_without_domain("/service/application/share/v1.0/links/short-link/{hash}/original/", hash=hash), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    

class FileStorage:
    def __init__(self, config):
        self._conf = config
        self._relativeUrls = {
            "startUpload": "/service/application/assets/v1.0/namespaces/{namespace}/upload/start/",
            "completeUpload": "/service/application/assets/v1.0/namespaces/{namespace}/upload/complete/",
            "signUrls": "/service/application/assets/v1.0/sign-urls/"
            
        }
        self._urls = {
            method: f"{self._conf.domain}{path}" for method, path in self._relativeUrls.items()
        }

    async def updateUrls(self, urls):
        self._urls.update(urls)
    
    async def startUpload(self, namespace=None, body=""):
        """Use this API to perform the first step of uploading (i.e. **Start**) an arbitrarily sized buffer or blob.

The three major steps are:
* Start
* Upload
* Complete

### Start
Initiates the assets upload using `startUpload`.
It returns a storage link in response.

### Upload
Use the storage link to upload a file (Buffer or Blob) to the File Storage.
Make a `PUT` request on storage link received from `startUpload` API with the file (Buffer or Blob) in the request body.

### Complete
After successfully upload, call the `completeUpload` API to finish the upload process.
This operation will return the URL of the uploaded file.

        :param namespace : Name of the bucket created for storing objects. : type string
        """
        payload = {}
        
        if namespace:
            payload["namespace"] = namespace
        
        # Parameter validation
        schema = FileStorageValidator.startUpload()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.StartRequest import StartRequest
        schema = StartRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["startUpload"], proccessed_params="""{"required":[{"name":"namespace","in":"path","description":"Name of the bucket created for storing objects.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"namespace","in":"path","description":"Name of the bucket created for storing objects.","required":true,"schema":{"type":"string"}}]}""", namespace=namespace)
        query_string = await create_query_string(namespace=namespace)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["startUpload"]).netloc, "post", await create_url_without_domain("/service/application/assets/v1.0/namespaces/{namespace}/upload/start/", namespace=namespace), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def completeUpload(self, namespace=None, body=""):
        """Use this API to perform the third step of uploading (i.e. **Complete**) an arbitrarily sized buffer or blob.

The three major steps are:
* Start
* Upload
* Complete

### Start
Initiates the assets upload using `startUpload`.
It returns a storage link in response.

### Upload
Use the storage link to upload a file (Buffer or Blob) to the File Storage.
Make a `PUT` request on storage link received from `startUpload` API with the file (Buffer or Blob) in the request body.

### Complete
After successfully upload, call the `completeUpload` API to finish the upload process.
This operation will return the URL of the uploaded file.

        :param namespace : Name of the bucket created for storing objects. : type string
        """
        payload = {}
        
        if namespace:
            payload["namespace"] = namespace
        
        # Parameter validation
        schema = FileStorageValidator.completeUpload()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.StartResponse import StartResponse
        schema = StartResponse()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["completeUpload"], proccessed_params="""{"required":[{"name":"namespace","in":"path","description":"Name of the bucket created for storing objects.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"namespace","in":"path","description":"Name of the bucket created for storing objects.","required":true,"schema":{"type":"string"}}]}""", namespace=namespace)
        query_string = await create_query_string(namespace=namespace)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["completeUpload"]).netloc, "post", await create_url_without_domain("/service/application/assets/v1.0/namespaces/{namespace}/upload/complete/", namespace=namespace), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def signUrls(self, body=""):
        """Describe here
        """
        payload = {}
        
        # Parameter validation
        schema = FileStorageValidator.signUrls()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.SignUrlRequest import SignUrlRequest
        schema = SignUrlRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["signUrls"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["signUrls"]).netloc, "post", await create_url_without_domain("/service/application/assets/v1.0/sign-urls/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    

class Configuration:
    def __init__(self, config):
        self._conf = config
        self._relativeUrls = {
            "getApplication": "/service/application/configuration/v1.0/application",
            "getOwnerInfo": "/service/application/configuration/v1.0/about",
            "getBasicDetails": "/service/application/configuration/v1.0/detail",
            "getIntegrationTokens": "/service/application/configuration/v1.0/token",
            "getOrderingStores": "/service/application/configuration/v1.0/ordering-store/stores",
            "getStoreDetailById": "/service/application/configuration/v1.0/ordering-store/stores/{store_id}",
            "getFeatures": "/service/application/configuration/v1.0/feature",
            "getContactInfo": "/service/application/configuration/v1.0/information",
            "getCurrencies": "/service/application/configuration/v1.0/currencies",
            "getCurrencyById": "/service/application/configuration/v1.0/currency/{id}",
            "getAppCurrencies": "/service/application/configuration/v1.0/currency",
            "getLanguages": "/service/application/configuration/v1.0/languages",
            "getOrderingStoreCookie": "/service/application/configuration/v1.0/ordering-store/select",
            "removeOrderingStoreCookie": "/service/application/configuration/v1.0/ordering-store/select",
            "getAppStaffList": "/service/application/configuration/v1.0/staff/list",
            "getAppStaffs": "/service/application/configuration/v1.0/staff"
            
        }
        self._urls = {
            method: f"{self._conf.domain}{path}" for method, path in self._relativeUrls.items()
        }

    async def updateUrls(self, urls):
        self._urls.update(urls)
    
    async def getApplication(self, body=""):
        """Use this API to get the current application details which includes configurations that indicate the status of the website, domain, ID, tokens, images, etc.
        """
        payload = {}
        
        # Parameter validation
        schema = ConfigurationValidator.getApplication()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getApplication"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getApplication"]).netloc, "get", await create_url_without_domain("/service/application/configuration/v1.0/application", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getOwnerInfo(self, body=""):
        """Use this API to get the current application details which includes channel name, description, banner, logo, favicon, domain details, etc. This API also retrieves the seller and owner information such as address, email address, and phone number.
        """
        payload = {}
        
        # Parameter validation
        schema = ConfigurationValidator.getOwnerInfo()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getOwnerInfo"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getOwnerInfo"]).netloc, "get", await create_url_without_domain("/service/application/configuration/v1.0/about", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getBasicDetails(self, body=""):
        """Use this API to retrieve only the basic details of the application which includes channel name, description, banner, logo, favicon, domain details, etc.
        """
        payload = {}
        
        # Parameter validation
        schema = ConfigurationValidator.getBasicDetails()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getBasicDetails"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getBasicDetails"]).netloc, "get", await create_url_without_domain("/service/application/configuration/v1.0/detail", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getIntegrationTokens(self, body=""):
        """Use this API to retrieve the tokens used while integrating Firebase, MoEngage, Segment, GTM, Freshchat, Safetynet, Google Map and Facebook. **Note** - Token values are encrypted with AES encryption using a secret key. Kindly reach out to the developers for obtaining the secret key.
        """
        payload = {}
        
        # Parameter validation
        schema = ConfigurationValidator.getIntegrationTokens()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getIntegrationTokens"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getIntegrationTokens"]).netloc, "get", await create_url_without_domain("/service/application/configuration/v1.0/token", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getOrderingStores(self, page_no=None, page_size=None, q=None, body=""):
        """Use this API to retrieve the details of all the deployment stores (the selling locations where the application will be utilized for placing orders).
        :param page_no : The page number to navigate through the given set of results. Default value is 1. : type integer
        :param page_size : The number of items to retrieve in each page. Default value is 10. : type integer
        :param q : Store code or name of the ordering store. : type string
        """
        payload = {}
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        
        if q:
            payload["q"] = q
        
        # Parameter validation
        schema = ConfigurationValidator.getOrderingStores()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getOrderingStores"], proccessed_params="""{"required":[],"optional":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"The page number to navigate through the given set of results. Default value is 1."},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"The number of items to retrieve in each page. Default value is 10."},{"name":"q","in":"query","schema":{"type":"string"},"description":"Store code or name of the ordering store."}],"query":[{"name":"page_no","in":"query","schema":{"type":"integer"},"description":"The page number to navigate through the given set of results. Default value is 1."},{"name":"page_size","in":"query","schema":{"type":"integer"},"description":"The number of items to retrieve in each page. Default value is 10."},{"name":"q","in":"query","schema":{"type":"string"},"description":"Store code or name of the ordering store."}],"headers":[],"path":[]}""", page_no=page_no, page_size=page_size, q=q)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, q=q)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getOrderingStores"]).netloc, "get", await create_url_without_domain("/service/application/configuration/v1.0/ordering-store/stores", page_no=page_no, page_size=page_size, q=q), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getStoreDetailById(self, store_id=None, body=""):
        """Use this API to retrieve the details of given stores uid (the selling locations where the application will be utilized for placing orders).
        :param store_id : Store uid : type integer
        """
        payload = {}
        
        if store_id:
            payload["store_id"] = store_id
        
        # Parameter validation
        schema = ConfigurationValidator.getStoreDetailById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getStoreDetailById"], proccessed_params="""{"required":[{"name":"store_id","in":"path","required":true,"description":"Store uid","schema":{"type":"integer"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"store_id","in":"path","required":true,"description":"Store uid","schema":{"type":"integer"}}]}""", store_id=store_id)
        query_string = await create_query_string(store_id=store_id)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getStoreDetailById"]).netloc, "get", await create_url_without_domain("/service/application/configuration/v1.0/ordering-store/stores/{store_id}", store_id=store_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getFeatures(self, body=""):
        """Use this API to retrieve the configuration of features such as product detail, landing page, options in the login/registration screen, communication opt-in, cart options and many more.
        """
        payload = {}
        
        # Parameter validation
        schema = ConfigurationValidator.getFeatures()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getFeatures"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getFeatures"]).netloc, "get", await create_url_without_domain("/service/application/configuration/v1.0/feature", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getContactInfo(self, body=""):
        """Use this API to retrieve information about the social links, address and contact information of the company/seller/brand operating the application.
        """
        payload = {}
        
        # Parameter validation
        schema = ConfigurationValidator.getContactInfo()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getContactInfo"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getContactInfo"]).netloc, "get", await create_url_without_domain("/service/application/configuration/v1.0/information", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getCurrencies(self, body=""):
        """Use this API to get a list of currencies available. Moreover, get the name, code, symbol, and the decimal digits of the currencies.
        """
        payload = {}
        
        # Parameter validation
        schema = ConfigurationValidator.getCurrencies()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getCurrencies"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getCurrencies"]).netloc, "get", await create_url_without_domain("/service/application/configuration/v1.0/currencies", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getCurrencyById(self, id=None, body=""):
        """Use this API to retrieve a currency using its ID.
        :param id : Object ID assigned to the currency : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        
        # Parameter validation
        schema = ConfigurationValidator.getCurrencyById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getCurrencyById"], proccessed_params="""{"required":[{"name":"id","in":"path","required":true,"description":"Object ID assigned to the currency","schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"id","in":"path","required":true,"description":"Object ID assigned to the currency","schema":{"type":"string"}}]}""", id=id)
        query_string = await create_query_string(id=id)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getCurrencyById"]).netloc, "get", await create_url_without_domain("/service/application/configuration/v1.0/currency/{id}", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getAppCurrencies(self, body=""):
        """Use this API to get a list of currencies allowed in the current application. Moreover, get the name, code, symbol, and the decimal digits of the currencies.
        """
        payload = {}
        
        # Parameter validation
        schema = ConfigurationValidator.getAppCurrencies()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getAppCurrencies"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getAppCurrencies"]).netloc, "get", await create_url_without_domain("/service/application/configuration/v1.0/currency", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getLanguages(self, body=""):
        """Use this API to get a list of languages supported in the application.
        """
        payload = {}
        
        # Parameter validation
        schema = ConfigurationValidator.getLanguages()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getLanguages"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getLanguages"]).netloc, "get", await create_url_without_domain("/service/application/configuration/v1.0/languages", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getOrderingStoreCookie(self, body=""):
        """Use this API to get an Ordering Store signed cookie upon selecting an ordering store. This will be used by the cart service to verify a coupon against the selected ordering store in cart.
        """
        payload = {}
        
        # Parameter validation
        schema = ConfigurationValidator.getOrderingStoreCookie()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.OrderingStoreSelectRequest import OrderingStoreSelectRequest
        schema = OrderingStoreSelectRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getOrderingStoreCookie"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getOrderingStoreCookie"]).netloc, "post", await create_url_without_domain("/service/application/configuration/v1.0/ordering-store/select", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def removeOrderingStoreCookie(self, body=""):
        """Use this API to unset the Ordering Store cookie upon changing the sales channel, by its domain URL, in the Universal Fynd Store app.
        """
        payload = {}
        
        # Parameter validation
        schema = ConfigurationValidator.removeOrderingStoreCookie()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["removeOrderingStoreCookie"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["removeOrderingStoreCookie"]).netloc, "delete", await create_url_without_domain("/service/application/configuration/v1.0/ordering-store/select", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getAppStaffList(self, page_no=None, page_size=None, order_incent=None, ordering_store=None, user=None, body=""):
        """Use this API to get a list of staff including the names, employee code, incentive status, assigned ordering stores, and title of each staff added to the application.
        :param page_no :  : type integer
        :param page_size :  : type integer
        :param order_incent : This is a boolean value. Select `true` to retrieve the staff members eligible for getting incentives on orders. : type boolean
        :param ordering_store : ID of the ordering store. Helps in retrieving staff members working at a particular ordering store. : type integer
        :param user : Mongo ID of the staff. Helps in retrieving the details of a particular staff member. : type string
        """
        payload = {}
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        
        if order_incent:
            payload["order_incent"] = order_incent
        
        if ordering_store:
            payload["ordering_store"] = ordering_store
        
        if user:
            payload["user"] = user
        
        # Parameter validation
        schema = ConfigurationValidator.getAppStaffList()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getAppStaffList"], proccessed_params="""{"required":[],"optional":[{"name":"page_no","in":"query","schema":{"type":"integer"}},{"name":"page_size","in":"query","schema":{"type":"integer"}},{"name":"order_incent","in":"query","description":"This is a boolean value. Select `true` to retrieve the staff members eligible for getting incentives on orders.","required":false,"schema":{"type":"boolean","example":true}},{"name":"ordering_store","in":"query","description":"ID of the ordering store. Helps in retrieving staff members working at a particular ordering store.","required":false,"schema":{"type":"integer","example":12}},{"name":"user","in":"query","description":"Mongo ID of the staff. Helps in retrieving the details of a particular staff member.","required":false,"schema":{"type":"string","example":"5e6b6ae7d450b1219ffdf3b2"}}],"query":[{"name":"page_no","in":"query","schema":{"type":"integer"}},{"name":"page_size","in":"query","schema":{"type":"integer"}},{"name":"order_incent","in":"query","description":"This is a boolean value. Select `true` to retrieve the staff members eligible for getting incentives on orders.","required":false,"schema":{"type":"boolean","example":true}},{"name":"ordering_store","in":"query","description":"ID of the ordering store. Helps in retrieving staff members working at a particular ordering store.","required":false,"schema":{"type":"integer","example":12}},{"name":"user","in":"query","description":"Mongo ID of the staff. Helps in retrieving the details of a particular staff member.","required":false,"schema":{"type":"string","example":"5e6b6ae7d450b1219ffdf3b2"}}],"headers":[],"path":[]}""", page_no=page_no, page_size=page_size, order_incent=order_incent, ordering_store=ordering_store, user=user)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, order_incent=order_incent, ordering_store=ordering_store, user=user)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getAppStaffList"]).netloc, "get", await create_url_without_domain("/service/application/configuration/v1.0/staff/list", page_no=page_no, page_size=page_size, order_incent=order_incent, ordering_store=ordering_store, user=user), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getAppStaffs(self, order_incent=None, ordering_store=None, user=None, body=""):
        """Use this API to get a list of staff including the names, employee code, incentive status, assigned ordering stores, and title of each staff added to the application.
        :param order_incent : This is a boolean value. Select `true` to retrieve the staff members eligible for getting incentives on orders. : type boolean
        :param ordering_store : ID of the ordering store. Helps in retrieving staff members working at a particular ordering store. : type integer
        :param user : Mongo ID of the staff. Helps in retrieving the details of a particular staff member. : type string
        """
        payload = {}
        
        if order_incent:
            payload["order_incent"] = order_incent
        
        if ordering_store:
            payload["ordering_store"] = ordering_store
        
        if user:
            payload["user"] = user
        
        # Parameter validation
        schema = ConfigurationValidator.getAppStaffs()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getAppStaffs"], proccessed_params="""{"required":[],"optional":[{"name":"order_incent","in":"query","description":"This is a boolean value. Select `true` to retrieve the staff members eligible for getting incentives on orders.","required":false,"schema":{"type":"boolean","example":true}},{"name":"ordering_store","in":"query","description":"ID of the ordering store. Helps in retrieving staff members working at a particular ordering store.","required":false,"schema":{"type":"integer","example":12}},{"name":"user","in":"query","description":"Mongo ID of the staff. Helps in retrieving the details of a particular staff member.","required":false,"schema":{"type":"string","example":"5e6b6ae7d450b1219ffdf3b2"}}],"query":[{"name":"order_incent","in":"query","description":"This is a boolean value. Select `true` to retrieve the staff members eligible for getting incentives on orders.","required":false,"schema":{"type":"boolean","example":true}},{"name":"ordering_store","in":"query","description":"ID of the ordering store. Helps in retrieving staff members working at a particular ordering store.","required":false,"schema":{"type":"integer","example":12}},{"name":"user","in":"query","description":"Mongo ID of the staff. Helps in retrieving the details of a particular staff member.","required":false,"schema":{"type":"string","example":"5e6b6ae7d450b1219ffdf3b2"}}],"headers":[],"path":[]}""", order_incent=order_incent, ordering_store=ordering_store, user=user)
        query_string = await create_query_string(order_incent=order_incent, ordering_store=ordering_store, user=user)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getAppStaffs"]).netloc, "get", await create_url_without_domain("/service/application/configuration/v1.0/staff", order_incent=order_incent, ordering_store=ordering_store, user=user), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    

class Payment:
    def __init__(self, config):
        self._conf = config
        self._relativeUrls = {
            "getAggregatorsConfig": "/service/application/payment/v1.0/config/aggregators/key",
            "attachCardToCustomer": "/service/application/payment/v1.0/card/attach",
            "getActiveCardAggregator": "/service/application/payment/v1.0/card/aggregator",
            "getActiveUserCards": "/service/application/payment/v1.0/cards",
            "deleteUserCard": "/service/application/payment/v1.0/card/remove",
            "verifyCustomerForPayment": "/service/application/payment/v1.0/payment/customer/validation",
            "verifyAndChargePayment": "/service/application/payment/v1.0/payment/confirm/charge",
            "initialisePayment": "/service/application/payment/v1.0/payment/request",
            "checkAndUpdatePaymentStatus": "/service/application/payment/v1.0/payment/confirm/polling",
            "getPaymentModeRoutes": "/service/application/payment/v1.0/payment/options",
            "getPosPaymentModeRoutes": "/service/application/payment/v1.0/payment/options/pos",
            "getRupifiBannerDetails": "/service/application/payment/v1.0/rupifi/banner",
            "getActiveRefundTransferModes": "/service/application/payment/v1.0/refund/transfer-mode",
            "enableOrDisableRefundTransferMode": "/service/application/payment/v1.0/refund/transfer-mode",
            "getUserBeneficiariesDetail": "/service/application/payment/v1.0/refund/user/beneficiary",
            "verifyIfscCode": "/service/application/payment/v1.0/ifsc-code/verify",
            "getOrderBeneficiariesDetail": "/service/application/payment/v1.0/refund/order/beneficiaries",
            "verifyOtpAndAddBeneficiaryForBank": "/service/application/payment/v1.0/refund/verification/bank",
            "addBeneficiaryDetails": "/service/application/payment/v1.0/refund/account",
            "addRefundBankAccountUsingOTP": "/service/application/payment/v1.0/refund/account/otp",
            "verifyOtpAndAddBeneficiaryForWallet": "/service/application/payment/v1.0/refund/verification/wallet",
            "updateDefaultBeneficiary": "/service/application/payment/v1.0/refund/beneficiary/default"
            
        }
        self._urls = {
            method: f"{self._conf.domain}{path}" for method, path in self._relativeUrls.items()
        }

    async def updateUrls(self, urls):
        self._urls.update(urls)
    
    async def getAggregatorsConfig(self, x_api_token=None, refresh=None, body=""):
        """Use this API to retrieve the payment gateway key, secrets, merchant, SDK/API details to complete a payment at front-end.
        :param x-api-token : Used for basic authentication. : type string
        :param refresh : This is a boolean value. Select `true` to remove temporary cache files on payment gateway and replace with the latest one. : type boolean
        """
        payload = {}
        
        if x_api_token:
            payload["x_api_token"] = x_api_token
        
        if refresh:
            payload["refresh"] = refresh
        
        # Parameter validation
        schema = PaymentValidator.getAggregatorsConfig()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getAggregatorsConfig"], proccessed_params="""{"required":[],"optional":[{"name":"x-api-token","in":"header","description":"Used for basic authentication.","required":false,"schema":{"type":"string"}},{"name":"refresh","in":"query","description":"This is a boolean value. Select `true` to remove temporary cache files on payment gateway and replace with the latest one.","schema":{"type":"boolean"}}],"query":[{"name":"refresh","in":"query","description":"This is a boolean value. Select `true` to remove temporary cache files on payment gateway and replace with the latest one.","schema":{"type":"boolean"}}],"headers":[{"name":"x-api-token","in":"header","description":"Used for basic authentication.","required":false,"schema":{"type":"string"}}],"path":[]}""", x_api_token=x_api_token, refresh=refresh)
        query_string = await create_query_string(x_api_token=x_api_token, refresh=refresh)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getAggregatorsConfig"]).netloc, "get", await create_url_without_domain("/service/application/payment/v1.0/config/aggregators/key", x_api_token=x_api_token, refresh=refresh), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def attachCardToCustomer(self, body=""):
        """Use this API to attach a customer's saved card at the payment gateway, such as Stripe, Juspay.
        """
        payload = {}
        
        # Parameter validation
        schema = PaymentValidator.attachCardToCustomer()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.AttachCardRequest import AttachCardRequest
        schema = AttachCardRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["attachCardToCustomer"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["attachCardToCustomer"]).netloc, "post", await create_url_without_domain("/service/application/payment/v1.0/card/attach", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getActiveCardAggregator(self, refresh=None, body=""):
        """Use this API to retrieve an active payment aggregator along with the Customer ID. This is applicable for cards payments only.
        :param refresh :  : type boolean
        """
        payload = {}
        
        if refresh:
            payload["refresh"] = refresh
        
        # Parameter validation
        schema = PaymentValidator.getActiveCardAggregator()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getActiveCardAggregator"], proccessed_params="""{"required":[],"optional":[{"in":"query","name":"refresh","schema":{"type":"boolean","default":false,"description":"This is a boolean value. Select `true` to remove temporary cache files on payment gateway and replace with the latest one."}}],"query":[{"in":"query","name":"refresh","schema":{"type":"boolean","default":false,"description":"This is a boolean value. Select `true` to remove temporary cache files on payment gateway and replace with the latest one."}}],"headers":[],"path":[]}""", refresh=refresh)
        query_string = await create_query_string(refresh=refresh)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getActiveCardAggregator"]).netloc, "get", await create_url_without_domain("/service/application/payment/v1.0/card/aggregator", refresh=refresh), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getActiveUserCards(self, force_refresh=None, body=""):
        """Use this API to retrieve a list of cards stored by user from an active payment gateway.
        :param force_refresh :  : type boolean
        """
        payload = {}
        
        if force_refresh:
            payload["force_refresh"] = force_refresh
        
        # Parameter validation
        schema = PaymentValidator.getActiveUserCards()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getActiveUserCards"], proccessed_params="""{"required":[],"optional":[{"in":"query","name":"force_refresh","schema":{"type":"boolean","default":false,"description":"This is a boolean value. Select `true` to clear the cache."}}],"query":[{"in":"query","name":"force_refresh","schema":{"type":"boolean","default":false,"description":"This is a boolean value. Select `true` to clear the cache."}}],"headers":[],"path":[]}""", force_refresh=force_refresh)
        query_string = await create_query_string(force_refresh=force_refresh)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getActiveUserCards"]).netloc, "get", await create_url_without_domain("/service/application/payment/v1.0/cards", force_refresh=force_refresh), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def deleteUserCard(self, body=""):
        """Use this API to delete a card added by a user on the payment gateway and clear the cache.
        """
        payload = {}
        
        # Parameter validation
        schema = PaymentValidator.deleteUserCard()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.DeletehCardRequest import DeletehCardRequest
        schema = DeletehCardRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["deleteUserCard"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["deleteUserCard"]).netloc, "post", await create_url_without_domain("/service/application/payment/v1.0/card/remove", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def verifyCustomerForPayment(self, body=""):
        """Use this API to check if the customer is eligible to use credit-line facilities such as Simpl Pay Later and Rupifi.
        """
        payload = {}
        
        # Parameter validation
        schema = PaymentValidator.verifyCustomerForPayment()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.ValidateCustomerRequest import ValidateCustomerRequest
        schema = ValidateCustomerRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["verifyCustomerForPayment"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["verifyCustomerForPayment"]).netloc, "post", await create_url_without_domain("/service/application/payment/v1.0/payment/customer/validation", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def verifyAndChargePayment(self, body=""):
        """Use this API to verify and check the status of a payment transaction (server-to-server) made through aggregators like Simpl and Mswipe.
        """
        payload = {}
        
        # Parameter validation
        schema = PaymentValidator.verifyAndChargePayment()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.ChargeCustomerRequest import ChargeCustomerRequest
        schema = ChargeCustomerRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["verifyAndChargePayment"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["verifyAndChargePayment"]).netloc, "post", await create_url_without_domain("/service/application/payment/v1.0/payment/confirm/charge", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def initialisePayment(self, body=""):
        """PUse this API to inititate payment using UPI, BharatQR, wherein the UPI requests are send to the app and QR code is displayed on the screen.
        """
        payload = {}
        
        # Parameter validation
        schema = PaymentValidator.initialisePayment()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.PaymentInitializationRequest import PaymentInitializationRequest
        schema = PaymentInitializationRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["initialisePayment"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["initialisePayment"]).netloc, "post", await create_url_without_domain("/service/application/payment/v1.0/payment/request", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def checkAndUpdatePaymentStatus(self, body=""):
        """Use this API to perform continuous polling at intervals to check the status of payment until timeout.
        """
        payload = {}
        
        # Parameter validation
        schema = PaymentValidator.checkAndUpdatePaymentStatus()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.PaymentStatusUpdateRequest import PaymentStatusUpdateRequest
        schema = PaymentStatusUpdateRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["checkAndUpdatePaymentStatus"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["checkAndUpdatePaymentStatus"]).netloc, "post", await create_url_without_domain("/service/application/payment/v1.0/payment/confirm/polling", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getPaymentModeRoutes(self, amount=None, cart_id=None, pincode=None, checkout_mode=None, refresh=None, card_reference=None, user_details=None, body=""):
        """Use this API to get all valid payment options for doing a payment.
        :param amount : Payable amount. : type integer
        :param cart_id : Identifier of the cart. : type string
        :param pincode : The PIN Code of the destination address, e.g. 400059 : type string
        :param checkout_mode : Option to checkout for self or for others. : type string
        :param refresh : This is a boolean value. Select `true` to remove temporary cache files on payment gateway and replace with the latest one. : type boolean
        :param card_reference : Card reference id of user's debit or credit card. : type string
        :param user_details : URIencoded JSON containing details of an anonymous user. : type string
        """
        payload = {}
        
        if amount:
            payload["amount"] = amount
        
        if cart_id:
            payload["cart_id"] = cart_id
        
        if pincode:
            payload["pincode"] = pincode
        
        if checkout_mode:
            payload["checkout_mode"] = checkout_mode
        
        if refresh:
            payload["refresh"] = refresh
        
        if card_reference:
            payload["card_reference"] = card_reference
        
        if user_details:
            payload["user_details"] = user_details
        
        # Parameter validation
        schema = PaymentValidator.getPaymentModeRoutes()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getPaymentModeRoutes"], proccessed_params="""{"required":[{"name":"amount","in":"query","description":"Payable amount.","required":true,"schema":{"type":"integer"}},{"name":"cart_id","in":"query","description":"Identifier of the cart.","required":true,"schema":{"type":"string"}},{"name":"pincode","in":"query","description":"The PIN Code of the destination address, e.g. 400059","required":true,"schema":{"type":"string"}},{"name":"checkout_mode","in":"query","description":"Option to checkout for self or for others.","required":true,"schema":{"type":"string"}}],"optional":[{"name":"refresh","in":"query","description":"This is a boolean value. Select `true` to remove temporary cache files on payment gateway and replace with the latest one.","schema":{"type":"boolean"}},{"name":"card_reference","in":"query","description":"Card reference id of user's debit or credit card.","schema":{"type":"string"}},{"name":"user_details","in":"query","description":"URIencoded JSON containing details of an anonymous user.","example":"%7B%22first_name%22:%22Fynd%22,%22last_name%22:%22Dummy%22,%22mobile%22:%229999999999%22,%22email%22:%22paymentsdummy@gofynd.com%22%7D","schema":{"type":"string"}}],"query":[{"name":"amount","in":"query","description":"Payable amount.","required":true,"schema":{"type":"integer"}},{"name":"cart_id","in":"query","description":"Identifier of the cart.","required":true,"schema":{"type":"string"}},{"name":"pincode","in":"query","description":"The PIN Code of the destination address, e.g. 400059","required":true,"schema":{"type":"string"}},{"name":"checkout_mode","in":"query","description":"Option to checkout for self or for others.","required":true,"schema":{"type":"string"}},{"name":"refresh","in":"query","description":"This is a boolean value. Select `true` to remove temporary cache files on payment gateway and replace with the latest one.","schema":{"type":"boolean"}},{"name":"card_reference","in":"query","description":"Card reference id of user's debit or credit card.","schema":{"type":"string"}},{"name":"user_details","in":"query","description":"URIencoded JSON containing details of an anonymous user.","example":"%7B%22first_name%22:%22Fynd%22,%22last_name%22:%22Dummy%22,%22mobile%22:%229999999999%22,%22email%22:%22paymentsdummy@gofynd.com%22%7D","schema":{"type":"string"}}],"headers":[],"path":[]}""", amount=amount, cart_id=cart_id, pincode=pincode, checkout_mode=checkout_mode, refresh=refresh, card_reference=card_reference, user_details=user_details)
        query_string = await create_query_string(amount=amount, cart_id=cart_id, pincode=pincode, checkout_mode=checkout_mode, refresh=refresh, card_reference=card_reference, user_details=user_details)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getPaymentModeRoutes"]).netloc, "get", await create_url_without_domain("/service/application/payment/v1.0/payment/options", amount=amount, cart_id=cart_id, pincode=pincode, checkout_mode=checkout_mode, refresh=refresh, card_reference=card_reference, user_details=user_details), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getPosPaymentModeRoutes(self, amount=None, cart_id=None, pincode=None, checkout_mode=None, refresh=None, card_reference=None, order_type=None, user_details=None, body=""):
        """Use this API to get all valid payment options for doing a payment in POS.
        :param amount : Payable amount. : type integer
        :param cart_id : Identifier of the cart. : type string
        :param pincode : The PIN Code of the destination address, e.g. 400059 : type string
        :param checkout_mode : Option to checkout for self or for others. : type string
        :param refresh : This is a boolean value. Select `true` to remove temporary cache files on payment gateway and replace with the latest one. : type boolean
        :param card_reference : Card reference id of user's debit or credit card. : type string
        :param order_type : The order type of shipment * HomeDelivery - If the customer wants the order home-delivered * PickAtStore - If the customer wants the handover of an order at the store itself. : type string
        :param user_details : URIencoded JSON containing details of an anonymous user. : type string
        """
        payload = {}
        
        if amount:
            payload["amount"] = amount
        
        if cart_id:
            payload["cart_id"] = cart_id
        
        if pincode:
            payload["pincode"] = pincode
        
        if checkout_mode:
            payload["checkout_mode"] = checkout_mode
        
        if refresh:
            payload["refresh"] = refresh
        
        if card_reference:
            payload["card_reference"] = card_reference
        
        if order_type:
            payload["order_type"] = order_type
        
        if user_details:
            payload["user_details"] = user_details
        
        # Parameter validation
        schema = PaymentValidator.getPosPaymentModeRoutes()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getPosPaymentModeRoutes"], proccessed_params="""{"required":[{"name":"amount","in":"query","description":"Payable amount.","required":true,"schema":{"type":"integer"}},{"name":"cart_id","in":"query","description":"Identifier of the cart.","required":true,"schema":{"type":"string"}},{"name":"pincode","in":"query","description":"The PIN Code of the destination address, e.g. 400059","required":true,"schema":{"type":"string"}},{"name":"checkout_mode","in":"query","description":"Option to checkout for self or for others.","required":true,"schema":{"type":"string"}},{"name":"order_type","in":"query","required":true,"description":"The order type of shipment * HomeDelivery - If the customer wants the order home-delivered * PickAtStore - If the customer wants the handover of an order at the store itself.","schema":{"type":"string"}}],"optional":[{"name":"refresh","in":"query","description":"This is a boolean value. Select `true` to remove temporary cache files on payment gateway and replace with the latest one.","schema":{"type":"boolean"}},{"name":"card_reference","in":"query","description":"Card reference id of user's debit or credit card.","schema":{"type":"string"}},{"name":"user_details","in":"query","description":"URIencoded JSON containing details of an anonymous user.","example":"%7B%22first_name%22:%22Fynd%22,%22last_name%22:%22Dummy%22,%22mobile%22:%229999999999%22,%22email%22:%22paymentsdummy@gofynd.com%22%7D","schema":{"type":"string"}}],"query":[{"name":"amount","in":"query","description":"Payable amount.","required":true,"schema":{"type":"integer"}},{"name":"cart_id","in":"query","description":"Identifier of the cart.","required":true,"schema":{"type":"string"}},{"name":"pincode","in":"query","description":"The PIN Code of the destination address, e.g. 400059","required":true,"schema":{"type":"string"}},{"name":"checkout_mode","in":"query","description":"Option to checkout for self or for others.","required":true,"schema":{"type":"string"}},{"name":"refresh","in":"query","description":"This is a boolean value. Select `true` to remove temporary cache files on payment gateway and replace with the latest one.","schema":{"type":"boolean"}},{"name":"card_reference","in":"query","description":"Card reference id of user's debit or credit card.","schema":{"type":"string"}},{"name":"order_type","in":"query","required":true,"description":"The order type of shipment * HomeDelivery - If the customer wants the order home-delivered * PickAtStore - If the customer wants the handover of an order at the store itself.","schema":{"type":"string"}},{"name":"user_details","in":"query","description":"URIencoded JSON containing details of an anonymous user.","example":"%7B%22first_name%22:%22Fynd%22,%22last_name%22:%22Dummy%22,%22mobile%22:%229999999999%22,%22email%22:%22paymentsdummy@gofynd.com%22%7D","schema":{"type":"string"}}],"headers":[],"path":[]}""", amount=amount, cart_id=cart_id, pincode=pincode, checkout_mode=checkout_mode, refresh=refresh, card_reference=card_reference, order_type=order_type, user_details=user_details)
        query_string = await create_query_string(amount=amount, cart_id=cart_id, pincode=pincode, checkout_mode=checkout_mode, refresh=refresh, card_reference=card_reference, order_type=order_type, user_details=user_details)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getPosPaymentModeRoutes"]).netloc, "get", await create_url_without_domain("/service/application/payment/v1.0/payment/options/pos", amount=amount, cart_id=cart_id, pincode=pincode, checkout_mode=checkout_mode, refresh=refresh, card_reference=card_reference, order_type=order_type, user_details=user_details), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getRupifiBannerDetails(self, body=""):
        """Get CreditLine Offer if user is tentatively approved by rupifi
        """
        payload = {}
        
        # Parameter validation
        schema = PaymentValidator.getRupifiBannerDetails()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getRupifiBannerDetails"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getRupifiBannerDetails"]).netloc, "get", await create_url_without_domain("/service/application/payment/v1.0/rupifi/banner", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getActiveRefundTransferModes(self, body=""):
        """Use this API to retrieve eligible refund modes (such as Netbanking) and add the beneficiary details.
        """
        payload = {}
        
        # Parameter validation
        schema = PaymentValidator.getActiveRefundTransferModes()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getActiveRefundTransferModes"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getActiveRefundTransferModes"]).netloc, "get", await create_url_without_domain("/service/application/payment/v1.0/refund/transfer-mode", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def enableOrDisableRefundTransferMode(self, body=""):
        """Activate or Deactivate Transfer Mode to collect Beneficiary Details for Refund
        """
        payload = {}
        
        # Parameter validation
        schema = PaymentValidator.enableOrDisableRefundTransferMode()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.UpdateRefundTransferModeRequest import UpdateRefundTransferModeRequest
        schema = UpdateRefundTransferModeRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["enableOrDisableRefundTransferMode"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["enableOrDisableRefundTransferMode"]).netloc, "put", await create_url_without_domain("/service/application/payment/v1.0/refund/transfer-mode", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getUserBeneficiariesDetail(self, order_id=None, body=""):
        """Use this API to get the details of all active beneficiary added by a user for refund.
        :param order_id : A unique number used for identifying and tracking your orders. : type string
        """
        payload = {}
        
        if order_id:
            payload["order_id"] = order_id
        
        # Parameter validation
        schema = PaymentValidator.getUserBeneficiariesDetail()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getUserBeneficiariesDetail"], proccessed_params="""{"required":[{"in":"query","description":"A unique number used for identifying and tracking your orders.","name":"order_id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[{"in":"query","description":"A unique number used for identifying and tracking your orders.","name":"order_id","required":true,"schema":{"type":"string"}}],"headers":[],"path":[]}""", order_id=order_id)
        query_string = await create_query_string(order_id=order_id)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getUserBeneficiariesDetail"]).netloc, "get", await create_url_without_domain("/service/application/payment/v1.0/refund/user/beneficiary", order_id=order_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def verifyIfscCode(self, ifsc_code=None, body=""):
        """Use this API to check whether the 11-digit IFSC code is valid and to fetch the bank details for refund.
        :param ifsc_code : A 11-digit alphanumeric code that uniquely identifies a bank branch. : type string
        """
        payload = {}
        
        if ifsc_code:
            payload["ifsc_code"] = ifsc_code
        
        # Parameter validation
        schema = PaymentValidator.verifyIfscCode()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["verifyIfscCode"], proccessed_params="""{"required":[],"optional":[{"in":"query","name":"ifsc_code","schema":{"type":"string"},"description":"A 11-digit alphanumeric code that uniquely identifies a bank branch."}],"query":[{"in":"query","name":"ifsc_code","schema":{"type":"string"},"description":"A 11-digit alphanumeric code that uniquely identifies a bank branch."}],"headers":[],"path":[]}""", ifsc_code=ifsc_code)
        query_string = await create_query_string(ifsc_code=ifsc_code)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["verifyIfscCode"]).netloc, "get", await create_url_without_domain("/service/application/payment/v1.0/ifsc-code/verify", ifsc_code=ifsc_code), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getOrderBeneficiariesDetail(self, order_id=None, body=""):
        """Use this API to get the details of all active beneficiary added by a user for refund.
        :param order_id : A unique number used for identifying and tracking your orders. : type string
        """
        payload = {}
        
        if order_id:
            payload["order_id"] = order_id
        
        # Parameter validation
        schema = PaymentValidator.getOrderBeneficiariesDetail()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getOrderBeneficiariesDetail"], proccessed_params="""{"required":[{"in":"query","description":"A unique number used for identifying and tracking your orders.","name":"order_id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[{"in":"query","description":"A unique number used for identifying and tracking your orders.","name":"order_id","required":true,"schema":{"type":"string"}}],"headers":[],"path":[]}""", order_id=order_id)
        query_string = await create_query_string(order_id=order_id)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getOrderBeneficiariesDetail"]).netloc, "get", await create_url_without_domain("/service/application/payment/v1.0/refund/order/beneficiaries", order_id=order_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def verifyOtpAndAddBeneficiaryForBank(self, body=""):
        """Use this API to perform an OTP validation before saving the beneficiary details added for a refund.
        """
        payload = {}
        
        # Parameter validation
        schema = PaymentValidator.verifyOtpAndAddBeneficiaryForBank()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.AddBeneficiaryViaOtpVerificationRequest import AddBeneficiaryViaOtpVerificationRequest
        schema = AddBeneficiaryViaOtpVerificationRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["verifyOtpAndAddBeneficiaryForBank"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["verifyOtpAndAddBeneficiaryForBank"]).netloc, "post", await create_url_without_domain("/service/application/payment/v1.0/refund/verification/bank", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def addBeneficiaryDetails(self, body=""):
        """Use this API to save the bank details for a returned or cancelled order to refund the amount.
        """
        payload = {}
        
        # Parameter validation
        schema = PaymentValidator.addBeneficiaryDetails()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.AddBeneficiaryDetailsRequest import AddBeneficiaryDetailsRequest
        schema = AddBeneficiaryDetailsRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["addBeneficiaryDetails"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["addBeneficiaryDetails"]).netloc, "post", await create_url_without_domain("/service/application/payment/v1.0/refund/account", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def addRefundBankAccountUsingOTP(self, body=""):
        """Use this API to save bank details for returned/cancelled order to refund amount in his account.
        """
        payload = {}
        
        # Parameter validation
        schema = PaymentValidator.addRefundBankAccountUsingOTP()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.AddBeneficiaryDetailsOTPRequest import AddBeneficiaryDetailsOTPRequest
        schema = AddBeneficiaryDetailsOTPRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["addRefundBankAccountUsingOTP"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["addRefundBankAccountUsingOTP"]).netloc, "post", await create_url_without_domain("/service/application/payment/v1.0/refund/account/otp", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def verifyOtpAndAddBeneficiaryForWallet(self, body=""):
        """Use this API to send an OTP while adding a wallet beneficiary by mobile no. verification.
        """
        payload = {}
        
        # Parameter validation
        schema = PaymentValidator.verifyOtpAndAddBeneficiaryForWallet()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.WalletOtpRequest import WalletOtpRequest
        schema = WalletOtpRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["verifyOtpAndAddBeneficiaryForWallet"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["verifyOtpAndAddBeneficiaryForWallet"]).netloc, "post", await create_url_without_domain("/service/application/payment/v1.0/refund/verification/wallet", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def updateDefaultBeneficiary(self, body=""):
        """Use this API to set a default beneficiary for getting a refund.
        """
        payload = {}
        
        # Parameter validation
        schema = PaymentValidator.updateDefaultBeneficiary()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.SetDefaultBeneficiaryRequest import SetDefaultBeneficiaryRequest
        schema = SetDefaultBeneficiaryRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["updateDefaultBeneficiary"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["updateDefaultBeneficiary"]).netloc, "post", await create_url_without_domain("/service/application/payment/v1.0/refund/beneficiary/default", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    

class Order:
    def __init__(self, config):
        self._conf = config
        self._relativeUrls = {
            "getOrders": "/service/application/order/v1.0/orders",
            "getOrderById": "/service/application/order/v1.0/orders/{order_id}",
            "getShipmentById": "/service/application/order/v1.0/orders/shipments/{shipment_id}",
            "getShipmentReasons": "/service/application/order/v1.0/orders/shipments/{shipment_id}/reasons",
            "updateShipmentStatus": "/service/application/order/v1.0/orders/shipments/{shipment_id}/status",
            "trackShipment": "/service/application/order/v1.0/orders/shipments/{shipment_id}/track",
            "getPosOrderById": "/service/application/order/v1.0/orders/pos-order/{order_id}",
            "getCustomerDetailsByShipmentId": "/service/application/order/v1.0/orders/{order_id}/shipments/{shipment_id}/customer-details",
            "sendOtpToShipmentCustomer": "/service/application/order/v1.0/orders/{order_id}/shipments/{shipment_id}/otp/send/",
            "verifyOtpShipmentCustomer": "/service/application/order/v1.0/orders/{order_id}/shipments/{shipment_id}/otp/verify",
            "getInvoiceByShipmentId": "/service/application/order/v1.0/orders/shipments/{shipment_id}/invoice"
            
        }
        self._urls = {
            method: f"{self._conf.domain}{path}" for method, path in self._relativeUrls.items()
        }

    async def updateUrls(self, urls):
        self._urls.update(urls)
    
    async def getOrders(self, page_no=None, page_size=None, from_date=None, to_date=None, status=None, body=""):
        """Use this API to retrieve all the orders.
        :param page_no : The page number to navigate through the given set of results. Default value is 1. : type integer
        :param page_size : The number of items to retrieve in each page. Default value is 10. : type integer
        :param from_date : The date from which the orders should be retrieved. : type string
        :param to_date : The date till which the orders should be retrieved. : type string
        :param status : A filter to retrieve orders by their current status such as _placed_, _delivered_, etc. : type integer
        """
        payload = {}
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        
        if from_date:
            payload["from_date"] = from_date
        
        if to_date:
            payload["to_date"] = to_date
        
        if status:
            payload["status"] = status
        
        # Parameter validation
        schema = OrderValidator.getOrders()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getOrders"], proccessed_params="""{"required":[],"optional":[{"name":"page_no","in":"query","description":"The page number to navigate through the given set of results. Default value is 1.","required":false,"schema":{"type":"integer"}},{"name":"page_size","in":"query","description":"The number of items to retrieve in each page. Default value is 10.","required":false,"schema":{"type":"integer"}},{"name":"from_date","in":"query","description":"The date from which the orders should be retrieved.","required":false,"schema":{"type":"string"}},{"name":"to_date","in":"query","description":"The date till which the orders should be retrieved.","required":false,"schema":{"type":"string"}},{"name":"status","in":"query","description":"A filter to retrieve orders by their current status such as _placed_, _delivered_, etc.","required":false,"schema":{"type":"integer"}}],"query":[{"name":"page_no","in":"query","description":"The page number to navigate through the given set of results. Default value is 1.","required":false,"schema":{"type":"integer"}},{"name":"page_size","in":"query","description":"The number of items to retrieve in each page. Default value is 10.","required":false,"schema":{"type":"integer"}},{"name":"from_date","in":"query","description":"The date from which the orders should be retrieved.","required":false,"schema":{"type":"string"}},{"name":"to_date","in":"query","description":"The date till which the orders should be retrieved.","required":false,"schema":{"type":"string"}},{"name":"status","in":"query","description":"A filter to retrieve orders by their current status such as _placed_, _delivered_, etc.","required":false,"schema":{"type":"integer"}}],"headers":[],"path":[]}""", page_no=page_no, page_size=page_size, from_date=from_date, to_date=to_date, status=status)
        query_string = await create_query_string(page_no=page_no, page_size=page_size, from_date=from_date, to_date=to_date, status=status)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getOrders"]).netloc, "get", await create_url_without_domain("/service/application/order/v1.0/orders", page_no=page_no, page_size=page_size, from_date=from_date, to_date=to_date, status=status), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getOrderById(self, order_id=None, body=""):
        """Use this API to retrieve order details such as tracking details, shipment, store information using Fynd Order ID.
        :param order_id : A unique number used for identifying and tracking your orders. : type string
        """
        payload = {}
        
        if order_id:
            payload["order_id"] = order_id
        
        # Parameter validation
        schema = OrderValidator.getOrderById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getOrderById"], proccessed_params="""{"required":[{"name":"order_id","in":"path","description":"A unique number used for identifying and tracking your orders.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"order_id","in":"path","description":"A unique number used for identifying and tracking your orders.","required":true,"schema":{"type":"string"}}]}""", order_id=order_id)
        query_string = await create_query_string(order_id=order_id)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getOrderById"]).netloc, "get", await create_url_without_domain("/service/application/order/v1.0/orders/{order_id}", order_id=order_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getShipmentById(self, shipment_id=None, body=""):
        """Use this API to retrieve shipment details such as price breakup, tracking details, store information, etc. using Shipment ID.
        :param shipment_id : ID of the shipment. An order may contain multiple items and may get divided into one or more shipment, each having its own ID. : type string
        """
        payload = {}
        
        if shipment_id:
            payload["shipment_id"] = shipment_id
        
        # Parameter validation
        schema = OrderValidator.getShipmentById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getShipmentById"], proccessed_params="""{"required":[{"name":"shipment_id","in":"path","description":"ID of the shipment. An order may contain multiple items and may get divided into one or more shipment, each having its own ID.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"shipment_id","in":"path","description":"ID of the shipment. An order may contain multiple items and may get divided into one or more shipment, each having its own ID.","required":true,"schema":{"type":"string"}}]}""", shipment_id=shipment_id)
        query_string = await create_query_string(shipment_id=shipment_id)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getShipmentById"]).netloc, "get", await create_url_without_domain("/service/application/order/v1.0/orders/shipments/{shipment_id}", shipment_id=shipment_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getShipmentReasons(self, shipment_id=None, body=""):
        """Use this API to retrieve the issues that led to the cancellation of bags within a shipment.
        :param shipment_id : ID of the shipment. An order may contain multiple items and may get divided into one or more shipment, each having its own ID. : type string
        """
        payload = {}
        
        if shipment_id:
            payload["shipment_id"] = shipment_id
        
        # Parameter validation
        schema = OrderValidator.getShipmentReasons()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getShipmentReasons"], proccessed_params="""{"required":[{"name":"shipment_id","in":"path","description":"ID of the shipment. An order may contain multiple items and may get divided into one or more shipment, each having its own ID.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"shipment_id","in":"path","description":"ID of the shipment. An order may contain multiple items and may get divided into one or more shipment, each having its own ID.","required":true,"schema":{"type":"string"}}]}""", shipment_id=shipment_id)
        query_string = await create_query_string(shipment_id=shipment_id)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getShipmentReasons"]).netloc, "get", await create_url_without_domain("/service/application/order/v1.0/orders/shipments/{shipment_id}/reasons", shipment_id=shipment_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def updateShipmentStatus(self, shipment_id=None, body=""):
        """Use this API to update the status of a shipment using its shipment ID.
        :param shipment_id : ID of the shipment. An order may contain multiple items and may get divided into one or more shipment, each having its own ID. : type string
        """
        payload = {}
        
        if shipment_id:
            payload["shipment_id"] = shipment_id
        
        # Parameter validation
        schema = OrderValidator.updateShipmentStatus()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.ShipmentStatusUpdateBody import ShipmentStatusUpdateBody
        schema = ShipmentStatusUpdateBody()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["updateShipmentStatus"], proccessed_params="""{"required":[{"name":"shipment_id","in":"path","description":"ID of the shipment. An order may contain multiple items and may get divided into one or more shipment, each having its own ID.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"shipment_id","in":"path","description":"ID of the shipment. An order may contain multiple items and may get divided into one or more shipment, each having its own ID.","required":true,"schema":{"type":"string"}}]}""", shipment_id=shipment_id)
        query_string = await create_query_string(shipment_id=shipment_id)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["updateShipmentStatus"]).netloc, "put", await create_url_without_domain("/service/application/order/v1.0/orders/shipments/{shipment_id}/status", shipment_id=shipment_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def trackShipment(self, shipment_id=None, body=""):
        """Use this API to track a shipment using its shipment ID.
        :param shipment_id : ID of the shipment. An order may contain multiple items and may get divided into one or more shipment, each having its own ID. : type string
        """
        payload = {}
        
        if shipment_id:
            payload["shipment_id"] = shipment_id
        
        # Parameter validation
        schema = OrderValidator.trackShipment()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["trackShipment"], proccessed_params="""{"required":[{"name":"shipment_id","in":"path","description":"ID of the shipment. An order may contain multiple items and may get divided into one or more shipment, each having its own ID.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"shipment_id","in":"path","description":"ID of the shipment. An order may contain multiple items and may get divided into one or more shipment, each having its own ID.","required":true,"schema":{"type":"string"}}]}""", shipment_id=shipment_id)
        query_string = await create_query_string(shipment_id=shipment_id)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["trackShipment"]).netloc, "get", await create_url_without_domain("/service/application/order/v1.0/orders/shipments/{shipment_id}/track", shipment_id=shipment_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getPosOrderById(self, order_id=None, body=""):
        """Use this API to retrieve a POS order and all its details such as tracking details, shipment, store information using Fynd Order ID.
        :param order_id : A unique number used for identifying and tracking your orders. : type string
        """
        payload = {}
        
        if order_id:
            payload["order_id"] = order_id
        
        # Parameter validation
        schema = OrderValidator.getPosOrderById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getPosOrderById"], proccessed_params="""{"required":[{"name":"order_id","in":"path","description":"A unique number used for identifying and tracking your orders.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"order_id","in":"path","description":"A unique number used for identifying and tracking your orders.","required":true,"schema":{"type":"string"}}]}""", order_id=order_id)
        query_string = await create_query_string(order_id=order_id)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getPosOrderById"]).netloc, "get", await create_url_without_domain("/service/application/order/v1.0/orders/pos-order/{order_id}", order_id=order_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getCustomerDetailsByShipmentId(self, order_id=None, shipment_id=None, body=""):
        """Use this API to retrieve customer details such as mobileno using Shipment ID.
        :param order_id : A unique number used for identifying and tracking your orders. : type string
        :param shipment_id : ID of the shipment. An order may contain multiple items and may get divided into one or more shipment, each having its own ID. : type string
        """
        payload = {}
        
        if order_id:
            payload["order_id"] = order_id
        
        if shipment_id:
            payload["shipment_id"] = shipment_id
        
        # Parameter validation
        schema = OrderValidator.getCustomerDetailsByShipmentId()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getCustomerDetailsByShipmentId"], proccessed_params="""{"required":[{"name":"order_id","in":"path","description":"A unique number used for identifying and tracking your orders.","required":true,"schema":{"type":"string"}},{"name":"shipment_id","in":"path","description":"ID of the shipment. An order may contain multiple items and may get divided into one or more shipment, each having its own ID.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"order_id","in":"path","description":"A unique number used for identifying and tracking your orders.","required":true,"schema":{"type":"string"}},{"name":"shipment_id","in":"path","description":"ID of the shipment. An order may contain multiple items and may get divided into one or more shipment, each having its own ID.","required":true,"schema":{"type":"string"}}]}""", order_id=order_id, shipment_id=shipment_id)
        query_string = await create_query_string(order_id=order_id, shipment_id=shipment_id)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getCustomerDetailsByShipmentId"]).netloc, "get", await create_url_without_domain("/service/application/order/v1.0/orders/{order_id}/shipments/{shipment_id}/customer-details", order_id=order_id, shipment_id=shipment_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def sendOtpToShipmentCustomer(self, order_id=None, shipment_id=None, body=""):
        """Use this API to send OTP to the customer of the mapped Shipment.
        :param order_id : A unique number used for identifying and tracking your orders. : type string
        :param shipment_id : ID of the shipment. An order may contain multiple items and may get divided into one or more shipment, each having its own ID. : type string
        """
        payload = {}
        
        if order_id:
            payload["order_id"] = order_id
        
        if shipment_id:
            payload["shipment_id"] = shipment_id
        
        # Parameter validation
        schema = OrderValidator.sendOtpToShipmentCustomer()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["sendOtpToShipmentCustomer"], proccessed_params="""{"required":[{"name":"order_id","in":"path","description":"A unique number used for identifying and tracking your orders.","required":true,"schema":{"type":"string"}},{"name":"shipment_id","in":"path","description":"ID of the shipment. An order may contain multiple items and may get divided into one or more shipment, each having its own ID.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"order_id","in":"path","description":"A unique number used for identifying and tracking your orders.","required":true,"schema":{"type":"string"}},{"name":"shipment_id","in":"path","description":"ID of the shipment. An order may contain multiple items and may get divided into one or more shipment, each having its own ID.","required":true,"schema":{"type":"string"}}]}""", order_id=order_id, shipment_id=shipment_id)
        query_string = await create_query_string(order_id=order_id, shipment_id=shipment_id)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["sendOtpToShipmentCustomer"]).netloc, "post", await create_url_without_domain("/service/application/order/v1.0/orders/{order_id}/shipments/{shipment_id}/otp/send/", order_id=order_id, shipment_id=shipment_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def verifyOtpShipmentCustomer(self, order_id=None, shipment_id=None, body=""):
        """Use this API to verify OTP and create a session token with custom payload.
        :param order_id : A unique number used for identifying and tracking your orders. : type string
        :param shipment_id : ID of the shipment. An order may contain multiple items and may get divided into one or more shipment, each having its own ID. : type string
        """
        payload = {}
        
        if order_id:
            payload["order_id"] = order_id
        
        if shipment_id:
            payload["shipment_id"] = shipment_id
        
        # Parameter validation
        schema = OrderValidator.verifyOtpShipmentCustomer()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.ReqBodyVerifyOTPShipment import ReqBodyVerifyOTPShipment
        schema = ReqBodyVerifyOTPShipment()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["verifyOtpShipmentCustomer"], proccessed_params="""{"required":[{"name":"order_id","in":"path","description":"A unique number used for identifying and tracking your orders.","required":true,"schema":{"type":"string"}},{"name":"shipment_id","in":"path","description":"ID of the shipment. An order may contain multiple items and may get divided into one or more shipment, each having its own ID.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"order_id","in":"path","description":"A unique number used for identifying and tracking your orders.","required":true,"schema":{"type":"string"}},{"name":"shipment_id","in":"path","description":"ID of the shipment. An order may contain multiple items and may get divided into one or more shipment, each having its own ID.","required":true,"schema":{"type":"string"}}]}""", order_id=order_id, shipment_id=shipment_id)
        query_string = await create_query_string(order_id=order_id, shipment_id=shipment_id)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["verifyOtpShipmentCustomer"]).netloc, "post", await create_url_without_domain("/service/application/order/v1.0/orders/{order_id}/shipments/{shipment_id}/otp/verify", order_id=order_id, shipment_id=shipment_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getInvoiceByShipmentId(self, shipment_id=None, body=""):
        """Use this API to get a generated Invoice URL for viewing or download.
        :param shipment_id : ID of the shipment. An order may contain multiple items and may get divided into one or more shipment, each having its own ID. : type string
        """
        payload = {}
        
        if shipment_id:
            payload["shipment_id"] = shipment_id
        
        # Parameter validation
        schema = OrderValidator.getInvoiceByShipmentId()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getInvoiceByShipmentId"], proccessed_params="""{"required":[{"name":"shipment_id","in":"path","description":"ID of the shipment. An order may contain multiple items and may get divided into one or more shipment, each having its own ID.","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"shipment_id","in":"path","description":"ID of the shipment. An order may contain multiple items and may get divided into one or more shipment, each having its own ID.","required":true,"schema":{"type":"string"}}]}""", shipment_id=shipment_id)
        query_string = await create_query_string(shipment_id=shipment_id)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getInvoiceByShipmentId"]).netloc, "get", await create_url_without_domain("/service/application/order/v1.0/orders/shipments/{shipment_id}/invoice", shipment_id=shipment_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    

class Rewards:
    def __init__(self, config):
        self._conf = config
        self._relativeUrls = {
            "getPointsOnProduct": "/service/application/rewards/v1.0/catalogue/offer/order/",
            "getOfferByName": "/service/application/rewards/v1.0/offers/{name}/",
            "getOrderDiscount": "/service/application/rewards/v1.0/user/offers/order-discount/",
            "getUserPoints": "/service/application/rewards/v1.0/user/points/",
            "getUserPointsHistory": "/service/application/rewards/v1.0/user/points/history/",
            "getUserReferralDetails": "/service/application/rewards/v1.0/user/referral/",
            "redeemReferralCode": "/service/application/rewards/v1.0/user/referral/redeem/"
            
        }
        self._urls = {
            method: f"{self._conf.domain}{path}" for method, path in self._relativeUrls.items()
        }

    async def updateUrls(self, urls):
        self._urls.update(urls)
    
    async def getPointsOnProduct(self, body=""):
        """Use this API to evaluate the amount of reward points that could be earned on any catalogue product.
        """
        payload = {}
        
        # Parameter validation
        schema = RewardsValidator.getPointsOnProduct()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.CatalogueOrderRequest import CatalogueOrderRequest
        schema = CatalogueOrderRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getPointsOnProduct"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getPointsOnProduct"]).netloc, "post", await create_url_without_domain("/service/application/rewards/v1.0/catalogue/offer/order/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getOfferByName(self, name=None, body=""):
        """Use this API to get the offer details and configuration by entering the name of the offer.
        :param name : The name given to the offer. : type string
        """
        payload = {}
        
        if name:
            payload["name"] = name
        
        # Parameter validation
        schema = RewardsValidator.getOfferByName()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getOfferByName"], proccessed_params="""{"required":[{"description":"The name given to the offer.","in":"path","name":"name","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"The name given to the offer.","in":"path","name":"name","required":true,"schema":{"type":"string"}}]}""", name=name)
        query_string = await create_query_string(name=name)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getOfferByName"]).netloc, "get", await create_url_without_domain("/service/application/rewards/v1.0/offers/{name}/", name=name), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getOrderDiscount(self, body=""):
        """Use this API to calculate the discount on order-amount based on all the amount range configured in order_discount.
        """
        payload = {}
        
        # Parameter validation
        schema = RewardsValidator.getOrderDiscount()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.OrderDiscountRequest import OrderDiscountRequest
        schema = OrderDiscountRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getOrderDiscount"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getOrderDiscount"]).netloc, "post", await create_url_without_domain("/service/application/rewards/v1.0/user/offers/order-discount/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getUserPoints(self, body=""):
        """Use this API to retrieve total available points of a user for current application
        """
        payload = {}
        
        # Parameter validation
        schema = RewardsValidator.getUserPoints()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getUserPoints"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getUserPoints"]).netloc, "get", await create_url_without_domain("/service/application/rewards/v1.0/user/points/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getUserPointsHistory(self, page_id=None, page_size=None, body=""):
        """Use this API to get a list of points transactions. The list of points history is paginated.
        :param page_id : PageID is the ID of the requested page. For first request it should be kept empty. : type string
        :param page_size : The number of items to retrieve in each page. : type integer
        """
        payload = {}
        
        if page_id:
            payload["page_id"] = page_id
        
        if page_size:
            payload["page_size"] = page_size
        
        # Parameter validation
        schema = RewardsValidator.getUserPointsHistory()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getUserPointsHistory"], proccessed_params="""{"required":[],"optional":[{"description":"PageID is the ID of the requested page. For first request it should be kept empty.","in":"query","name":"page_id","schema":{"type":"string"}},{"description":"The number of items to retrieve in each page.","in":"query","name":"page_size","schema":{"type":"integer"}}],"query":[{"description":"PageID is the ID of the requested page. For first request it should be kept empty.","in":"query","name":"page_id","schema":{"type":"string"}},{"description":"The number of items to retrieve in each page.","in":"query","name":"page_size","schema":{"type":"integer"}}],"headers":[],"path":[]}""", page_id=page_id, page_size=page_size)
        query_string = await create_query_string(page_id=page_id, page_size=page_size)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getUserPointsHistory"]).netloc, "get", await create_url_without_domain("/service/application/rewards/v1.0/user/points/history/", page_id=page_id, page_size=page_size), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getUserReferralDetails(self, body=""):
        """Use this API to retrieve the referral details a user has configured in the application.
        """
        payload = {}
        
        # Parameter validation
        schema = RewardsValidator.getUserReferralDetails()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getUserReferralDetails"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getUserReferralDetails"]).netloc, "get", await create_url_without_domain("/service/application/rewards/v1.0/user/referral/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def redeemReferralCode(self, body=""):
        """Use this API to enter a referral code following which, the configured points would be credited to a user's reward points account.
        """
        payload = {}
        
        # Parameter validation
        schema = RewardsValidator.redeemReferralCode()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.RedeemReferralCodeRequest import RedeemReferralCodeRequest
        schema = RedeemReferralCodeRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["redeemReferralCode"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["redeemReferralCode"]).netloc, "post", await create_url_without_domain("/service/application/rewards/v1.0/user/referral/redeem/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    

class Feedback:
    def __init__(self, config):
        self._conf = config
        self._relativeUrls = {
            "createAbuseReport": "/service/application/feedback/v1.0/abuse/",
            "updateAbuseReport": "/service/application/feedback/v1.0/abuse/",
            "getAbuseReports": "/service/application/feedback/v1.0/abuse/entity/{entity_type}/entity-id/{entity_id}",
            "getAttributes": "/service/application/feedback/v1.0/attributes/",
            "createAttribute": "/service/application/feedback/v1.0/attributes/",
            "getAttribute": "/service/application/feedback/v1.0/attributes/{slug}",
            "updateAttribute": "/service/application/feedback/v1.0/attributes/{slug}",
            "createComment": "/service/application/feedback/v1.0/comment/",
            "updateComment": "/service/application/feedback/v1.0/comment/",
            "getComments": "/service/application/feedback/v1.0/comment/entity/{entity_type}",
            "checkEligibility": "/service/application/feedback/v1.0/config/entity/{entity_type}/entity-id/{entity_id}",
            "deleteMedia": "/service/application/feedback/v1.0/media/",
            "createMedia": "/service/application/feedback/v1.0/media/",
            "updateMedia": "/service/application/feedback/v1.0/media/",
            "getMedias": "/service/application/feedback/v1.0/media/entity/{entity_type}/entity-id/{entity_id}",
            "getReviewSummaries": "/service/application/feedback/v1.0/rating/summary/entity/{entity_type}/entity-id/{entity_id}",
            "createReview": "/service/application/feedback/v1.0/review/",
            "updateReview": "/service/application/feedback/v1.0/review/",
            "getReviews": "/service/application/feedback/v1.0/review/entity/{entity_type}/entity-id/{entity_id}",
            "getTemplates": "/service/application/feedback/v1.0/template/",
            "createQuestion": "/service/application/feedback/v1.0/template/qna/",
            "updateQuestion": "/service/application/feedback/v1.0/template/qna/",
            "getQuestionAndAnswers": "/service/application/feedback/v1.0/template/qna/entity/{entity_type}/entity-id/{entity_id}",
            "getVotes": "/service/application/feedback/v1.0/vote/",
            "createVote": "/service/application/feedback/v1.0/vote/",
            "updateVote": "/service/application/feedback/v1.0/vote/"
            
        }
        self._urls = {
            method: f"{self._conf.domain}{path}" for method, path in self._relativeUrls.items()
        }

    async def updateUrls(self, urls):
        self._urls.update(urls)
    
    async def createAbuseReport(self, body=""):
        """Use this API to report a specific entity (question/review/comment) for abuse.
        """
        payload = {}
        
        # Parameter validation
        schema = FeedbackValidator.createAbuseReport()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.ReportAbuseRequest import ReportAbuseRequest
        schema = ReportAbuseRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["createAbuseReport"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["createAbuseReport"]).netloc, "post", await create_url_without_domain("/service/application/feedback/v1.0/abuse/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def updateAbuseReport(self, body=""):
        """Use this API to update the abuse details, i.e. status and description.
        """
        payload = {}
        
        # Parameter validation
        schema = FeedbackValidator.updateAbuseReport()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.UpdateAbuseStatusRequest import UpdateAbuseStatusRequest
        schema = UpdateAbuseStatusRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["updateAbuseReport"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["updateAbuseReport"]).netloc, "put", await create_url_without_domain("/service/application/feedback/v1.0/abuse/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getAbuseReports(self, entity_id=None, entity_type=None, id=None, page_id=None, page_size=None, body=""):
        """Use this API to retrieve a list of abuse data from entity type and entity ID.
        :param entity_id : ID of the eligible entity as specified in the entity type (question ID/review ID/comment ID). : type string
        :param entity_type : Type of entity, e.g. question, review or comment. : type string
        :param id : abuse id : type string
        :param page_id : Pagination page ID to retrieve next set of results. : type string
        :param page_size : The number of items to retrieve in each page. : type integer
        """
        payload = {}
        
        if entity_id:
            payload["entity_id"] = entity_id
        
        if entity_type:
            payload["entity_type"] = entity_type
        
        if id:
            payload["id"] = id
        
        if page_id:
            payload["page_id"] = page_id
        
        if page_size:
            payload["page_size"] = page_size
        
        # Parameter validation
        schema = FeedbackValidator.getAbuseReports()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getAbuseReports"], proccessed_params="""{"required":[{"description":"ID of the eligible entity as specified in the entity type (question ID/review ID/comment ID).","in":"path","name":"entity_id","required":true,"schema":{"type":"string"}},{"description":"Type of entity, e.g. question, review or comment.","in":"path","name":"entity_type","required":true,"schema":{"type":"string"}}],"optional":[{"description":"abuse id","in":"query","name":"id","schema":{"type":"string"}},{"description":"Pagination page ID to retrieve next set of results.","in":"query","name":"page_id","schema":{"type":"string"}},{"description":"The number of items to retrieve in each page.","in":"query","name":"page_size","schema":{"type":"integer"}}],"query":[{"description":"abuse id","in":"query","name":"id","schema":{"type":"string"}},{"description":"Pagination page ID to retrieve next set of results.","in":"query","name":"page_id","schema":{"type":"string"}},{"description":"The number of items to retrieve in each page.","in":"query","name":"page_size","schema":{"type":"integer"}}],"headers":[],"path":[{"description":"ID of the eligible entity as specified in the entity type (question ID/review ID/comment ID).","in":"path","name":"entity_id","required":true,"schema":{"type":"string"}},{"description":"Type of entity, e.g. question, review or comment.","in":"path","name":"entity_type","required":true,"schema":{"type":"string"}}]}""", entity_id=entity_id, entity_type=entity_type, id=id, page_id=page_id, page_size=page_size)
        query_string = await create_query_string(entity_id=entity_id, entity_type=entity_type, id=id, page_id=page_id, page_size=page_size)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getAbuseReports"]).netloc, "get", await create_url_without_domain("/service/application/feedback/v1.0/abuse/entity/{entity_type}/entity-id/{entity_id}", entity_id=entity_id, entity_type=entity_type, id=id, page_id=page_id, page_size=page_size), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getAttributes(self, page_no=None, page_size=None, body=""):
        """Use this API to retrieve a list of all attribute data, e.g. quality, material, product fitting, packaging, etc.
        :param page_no : The page number to navigate through the given set of results. Default value is 1.  : type integer
        :param page_size : The number of items to retrieve in each page. : type integer
        """
        payload = {}
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        
        # Parameter validation
        schema = FeedbackValidator.getAttributes()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getAttributes"], proccessed_params="""{"required":[],"optional":[{"description":"The page number to navigate through the given set of results. Default value is 1. ","in":"query","name":"page_no","schema":{"type":"integer"}},{"description":"The number of items to retrieve in each page.","in":"query","name":"page_size","schema":{"type":"integer"}}],"query":[{"description":"The page number to navigate through the given set of results. Default value is 1. ","in":"query","name":"page_no","schema":{"type":"integer"}},{"description":"The number of items to retrieve in each page.","in":"query","name":"page_size","schema":{"type":"integer"}}],"headers":[],"path":[]}""", page_no=page_no, page_size=page_size)
        query_string = await create_query_string(page_no=page_no, page_size=page_size)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getAttributes"]).netloc, "get", await create_url_without_domain("/service/application/feedback/v1.0/attributes/", page_no=page_no, page_size=page_size), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def createAttribute(self, body=""):
        """Use this API to add a new attribute (e.g. product quality/material/value for money) with its name, slug and description.
        """
        payload = {}
        
        # Parameter validation
        schema = FeedbackValidator.createAttribute()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.SaveAttributeRequest import SaveAttributeRequest
        schema = SaveAttributeRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["createAttribute"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["createAttribute"]).netloc, "post", await create_url_without_domain("/service/application/feedback/v1.0/attributes/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getAttribute(self, slug=None, body=""):
        """Use this API to retrieve a single attribute data from a given slug.
        :param slug : A short, human-readable, URL-friendly identifier of an attribute. You can get slug value from the endpoint 'service/application/feedback/v1.0/attributes'. : type string
        """
        payload = {}
        
        if slug:
            payload["slug"] = slug
        
        # Parameter validation
        schema = FeedbackValidator.getAttribute()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getAttribute"], proccessed_params="""{"required":[{"description":"A short, human-readable, URL-friendly identifier of an attribute. You can get slug value from the endpoint 'service/application/feedback/v1.0/attributes'.","in":"path","name":"slug","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A short, human-readable, URL-friendly identifier of an attribute. You can get slug value from the endpoint 'service/application/feedback/v1.0/attributes'.","in":"path","name":"slug","required":true,"schema":{"type":"string"}}]}""", slug=slug)
        query_string = await create_query_string(slug=slug)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getAttribute"]).netloc, "get", await create_url_without_domain("/service/application/feedback/v1.0/attributes/{slug}", slug=slug), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def updateAttribute(self, slug=None, body=""):
        """Use this API update the attribute's name and description.
        :param slug : A short, human-readable, URL-friendly identifier of an attribute. You can get slug value from the endpoint 'service/application/feedback/v1.0/attributes'. : type string
        """
        payload = {}
        
        if slug:
            payload["slug"] = slug
        
        # Parameter validation
        schema = FeedbackValidator.updateAttribute()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.UpdateAttributeRequest import UpdateAttributeRequest
        schema = UpdateAttributeRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["updateAttribute"], proccessed_params="""{"required":[{"description":"A short, human-readable, URL-friendly identifier of an attribute. You can get slug value from the endpoint 'service/application/feedback/v1.0/attributes'.","in":"path","name":"slug","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"A short, human-readable, URL-friendly identifier of an attribute. You can get slug value from the endpoint 'service/application/feedback/v1.0/attributes'.","in":"path","name":"slug","required":true,"schema":{"type":"string"}}]}""", slug=slug)
        query_string = await create_query_string(slug=slug)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["updateAttribute"]).netloc, "put", await create_url_without_domain("/service/application/feedback/v1.0/attributes/{slug}", slug=slug), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def createComment(self, body=""):
        """Use this API to add a new comment for a specific entity.
        """
        payload = {}
        
        # Parameter validation
        schema = FeedbackValidator.createComment()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.CommentRequest import CommentRequest
        schema = CommentRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["createComment"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["createComment"]).netloc, "post", await create_url_without_domain("/service/application/feedback/v1.0/comment/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def updateComment(self, body=""):
        """Use this API to update the comment status (active or approve) along with new comment if any.
        """
        payload = {}
        
        # Parameter validation
        schema = FeedbackValidator.updateComment()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.UpdateCommentRequest import UpdateCommentRequest
        schema = UpdateCommentRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["updateComment"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["updateComment"]).netloc, "put", await create_url_without_domain("/service/application/feedback/v1.0/comment/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getComments(self, entity_type=None, id=None, entity_id=None, user_id=None, page_id=None, page_size=None, body=""):
        """Use this API to retrieve a list of comments for a specific entity type, e.g. products.
        :param entity_type : Type of entity, e.g. question, review or comment. : type string
        :param id : Comment ID : type string
        :param entity_id : ID of the eligible entity as specified in the entity type (question ID/review ID/comment ID). : type string
        :param user_id : User ID - a flag/filter to get comments for a user. : type string
        :param page_id : Pagination page ID to retrieve next set of results. : type string
        :param page_size : The number of items to retrieve in each page. : type integer
        """
        payload = {}
        
        if entity_type:
            payload["entity_type"] = entity_type
        
        if id:
            payload["id"] = id
        
        if entity_id:
            payload["entity_id"] = entity_id
        
        if user_id:
            payload["user_id"] = user_id
        
        if page_id:
            payload["page_id"] = page_id
        
        if page_size:
            payload["page_size"] = page_size
        
        # Parameter validation
        schema = FeedbackValidator.getComments()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getComments"], proccessed_params="""{"required":[{"description":"Type of entity, e.g. question, review or comment.","in":"path","name":"entity_type","required":true,"schema":{"type":"string"}}],"optional":[{"description":"Comment ID","in":"query","name":"id","schema":{"type":"string"}},{"description":"ID of the eligible entity as specified in the entity type (question ID/review ID/comment ID).","in":"query","name":"entity_id","schema":{"type":"string"}},{"description":"User ID - a flag/filter to get comments for a user.","in":"query","name":"user_id","schema":{"type":"string"}},{"description":"Pagination page ID to retrieve next set of results.","in":"query","name":"page_id","schema":{"type":"string"}},{"description":"The number of items to retrieve in each page.","in":"query","name":"page_size","schema":{"type":"integer"}}],"query":[{"description":"Comment ID","in":"query","name":"id","schema":{"type":"string"}},{"description":"ID of the eligible entity as specified in the entity type (question ID/review ID/comment ID).","in":"query","name":"entity_id","schema":{"type":"string"}},{"description":"User ID - a flag/filter to get comments for a user.","in":"query","name":"user_id","schema":{"type":"string"}},{"description":"Pagination page ID to retrieve next set of results.","in":"query","name":"page_id","schema":{"type":"string"}},{"description":"The number of items to retrieve in each page.","in":"query","name":"page_size","schema":{"type":"integer"}}],"headers":[],"path":[{"description":"Type of entity, e.g. question, review or comment.","in":"path","name":"entity_type","required":true,"schema":{"type":"string"}}]}""", entity_type=entity_type, id=id, entity_id=entity_id, user_id=user_id, page_id=page_id, page_size=page_size)
        query_string = await create_query_string(entity_type=entity_type, id=id, entity_id=entity_id, user_id=user_id, page_id=page_id, page_size=page_size)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getComments"]).netloc, "get", await create_url_without_domain("/service/application/feedback/v1.0/comment/entity/{entity_type}", entity_type=entity_type, id=id, entity_id=entity_id, user_id=user_id, page_id=page_id, page_size=page_size), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def checkEligibility(self, entity_type=None, entity_id=None, body=""):
        """Use this API to check whether an entity is eligible to be rated and reviewed. Moreover, it shows the cloud media configuration too.
        :param entity_type : Type of entity, e.g. question, rate, review, answer, or comment. : type string
        :param entity_id : ID of the eligible entity as specified in the entity type. : type string
        """
        payload = {}
        
        if entity_type:
            payload["entity_type"] = entity_type
        
        if entity_id:
            payload["entity_id"] = entity_id
        
        # Parameter validation
        schema = FeedbackValidator.checkEligibility()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["checkEligibility"], proccessed_params="""{"required":[{"description":"Type of entity, e.g. question, rate, review, answer, or comment.","in":"path","name":"entity_type","required":true,"schema":{"type":"string"}},{"description":"ID of the eligible entity as specified in the entity type.","in":"path","name":"entity_id","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"description":"Type of entity, e.g. question, rate, review, answer, or comment.","in":"path","name":"entity_type","required":true,"schema":{"type":"string"}},{"description":"ID of the eligible entity as specified in the entity type.","in":"path","name":"entity_id","required":true,"schema":{"type":"string"}}]}""", entity_type=entity_type, entity_id=entity_id)
        query_string = await create_query_string(entity_type=entity_type, entity_id=entity_id)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["checkEligibility"]).netloc, "get", await create_url_without_domain("/service/application/feedback/v1.0/config/entity/{entity_type}/entity-id/{entity_id}", entity_type=entity_type, entity_id=entity_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def deleteMedia(self, ids=None, body=""):
        """Use this API to delete media for an entity ID.
        :param ids : List of media ID : type array
        """
        payload = {}
        
        if ids:
            payload["ids"] = ids
        
        # Parameter validation
        schema = FeedbackValidator.deleteMedia()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["deleteMedia"], proccessed_params="""{"required":[{"description":"List of media ID","in":"query","name":"ids","required":true,"schema":{"items":{"type":"string"},"type":"array"}}],"optional":[],"query":[{"description":"List of media ID","in":"query","name":"ids","required":true,"schema":{"items":{"type":"string"},"type":"array"}}],"headers":[],"path":[]}""", ids=ids)
        query_string = await create_query_string(ids=ids)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["deleteMedia"]).netloc, "delete", await create_url_without_domain("/service/application/feedback/v1.0/media/", ids=ids), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def createMedia(self, body=""):
        """Use this API to add media to an entity, e.g. review.
        """
        payload = {}
        
        # Parameter validation
        schema = FeedbackValidator.createMedia()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.AddMediaListRequest import AddMediaListRequest
        schema = AddMediaListRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["createMedia"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["createMedia"]).netloc, "post", await create_url_without_domain("/service/application/feedback/v1.0/media/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def updateMedia(self, body=""):
        """Use this API to update media (archive/approve) for an entity.
        """
        payload = {}
        
        # Parameter validation
        schema = FeedbackValidator.updateMedia()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.UpdateMediaListRequest import UpdateMediaListRequest
        schema = UpdateMediaListRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["updateMedia"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["updateMedia"]).netloc, "put", await create_url_without_domain("/service/application/feedback/v1.0/media/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getMedias(self, entity_type=None, entity_id=None, id=None, type=None, page_id=None, page_size=None, body=""):
        """Use this API to retrieve all media from an entity.
        :param entity_type : Type of entity, e.g. question or product. : type string
        :param entity_id : ID of the eligible entity as specified in the entity type(question ID/product ID). : type string
        :param id : ID of the media. : type string
        :param type : Media type. : type string
        :param page_id : Pagination page ID to retrieve next set of results. : type string
        :param page_size : The number of items to retrieve in each page. : type integer
        """
        payload = {}
        
        if entity_type:
            payload["entity_type"] = entity_type
        
        if entity_id:
            payload["entity_id"] = entity_id
        
        if id:
            payload["id"] = id
        
        if type:
            payload["type"] = type
        
        if page_id:
            payload["page_id"] = page_id
        
        if page_size:
            payload["page_size"] = page_size
        
        # Parameter validation
        schema = FeedbackValidator.getMedias()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getMedias"], proccessed_params="""{"required":[{"description":"Type of entity, e.g. question or product.","in":"path","name":"entity_type","required":true,"schema":{"type":"string"}},{"description":"ID of the eligible entity as specified in the entity type(question ID/product ID).","in":"path","name":"entity_id","required":true,"schema":{"type":"string"}}],"optional":[{"description":"ID of the media.","in":"query","name":"id","schema":{"type":"string"}},{"description":"Media type.","in":"query","name":"type","schema":{"type":"string"}},{"description":"Pagination page ID to retrieve next set of results.","in":"query","name":"page_id","schema":{"type":"string"}},{"description":"The number of items to retrieve in each page.","in":"query","name":"page_size","schema":{"type":"integer"}}],"query":[{"description":"ID of the media.","in":"query","name":"id","schema":{"type":"string"}},{"description":"Media type.","in":"query","name":"type","schema":{"type":"string"}},{"description":"Pagination page ID to retrieve next set of results.","in":"query","name":"page_id","schema":{"type":"string"}},{"description":"The number of items to retrieve in each page.","in":"query","name":"page_size","schema":{"type":"integer"}}],"headers":[],"path":[{"description":"Type of entity, e.g. question or product.","in":"path","name":"entity_type","required":true,"schema":{"type":"string"}},{"description":"ID of the eligible entity as specified in the entity type(question ID/product ID).","in":"path","name":"entity_id","required":true,"schema":{"type":"string"}}]}""", entity_type=entity_type, entity_id=entity_id, id=id, type=type, page_id=page_id, page_size=page_size)
        query_string = await create_query_string(entity_type=entity_type, entity_id=entity_id, id=id, type=type, page_id=page_id, page_size=page_size)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getMedias"]).netloc, "get", await create_url_without_domain("/service/application/feedback/v1.0/media/entity/{entity_type}/entity-id/{entity_id}", entity_type=entity_type, entity_id=entity_id, id=id, type=type, page_id=page_id, page_size=page_size), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getReviewSummaries(self, entity_type=None, entity_id=None, id=None, page_id=None, page_size=None, body=""):
        """Review summary gives ratings and attribute metrics of a review per entity. Use this API to retrieve the following response data: review count, rating average. 'review metrics'/'attribute rating metrics' which contains name, type, average and count.
        :param entity_type : Type of entity, e.g. product, delivery, seller, order placed, order delivered, application, or template. : type string
        :param entity_id : ID of the eligible entity as specified in the entity type. : type string
        :param id : Review summary identifier. : type string
        :param page_id : Pagination page ID to retrieve next set of results. : type string
        :param page_size : The number of items to retrieve in each page. : type integer
        """
        payload = {}
        
        if entity_type:
            payload["entity_type"] = entity_type
        
        if entity_id:
            payload["entity_id"] = entity_id
        
        if id:
            payload["id"] = id
        
        if page_id:
            payload["page_id"] = page_id
        
        if page_size:
            payload["page_size"] = page_size
        
        # Parameter validation
        schema = FeedbackValidator.getReviewSummaries()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getReviewSummaries"], proccessed_params="""{"required":[{"description":"Type of entity, e.g. product, delivery, seller, order placed, order delivered, application, or template.","in":"path","name":"entity_type","required":true,"schema":{"type":"string"}},{"description":"ID of the eligible entity as specified in the entity type.","in":"path","name":"entity_id","required":true,"schema":{"type":"string"}}],"optional":[{"description":"Review summary identifier.","in":"query","name":"id","schema":{"type":"string"}},{"description":"Pagination page ID to retrieve next set of results.","in":"query","name":"page_id","schema":{"type":"string"}},{"description":"The number of items to retrieve in each page.","in":"query","name":"page_size","schema":{"type":"integer"}}],"query":[{"description":"Review summary identifier.","in":"query","name":"id","schema":{"type":"string"}},{"description":"Pagination page ID to retrieve next set of results.","in":"query","name":"page_id","schema":{"type":"string"}},{"description":"The number of items to retrieve in each page.","in":"query","name":"page_size","schema":{"type":"integer"}}],"headers":[],"path":[{"description":"Type of entity, e.g. product, delivery, seller, order placed, order delivered, application, or template.","in":"path","name":"entity_type","required":true,"schema":{"type":"string"}},{"description":"ID of the eligible entity as specified in the entity type.","in":"path","name":"entity_id","required":true,"schema":{"type":"string"}}]}""", entity_type=entity_type, entity_id=entity_id, id=id, page_id=page_id, page_size=page_size)
        query_string = await create_query_string(entity_type=entity_type, entity_id=entity_id, id=id, page_id=page_id, page_size=page_size)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getReviewSummaries"]).netloc, "get", await create_url_without_domain("/service/application/feedback/v1.0/rating/summary/entity/{entity_type}/entity-id/{entity_id}", entity_type=entity_type, entity_id=entity_id, id=id, page_id=page_id, page_size=page_size), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def createReview(self, body=""):
        """Use this API to add customer reviews for a specific entity along with the following data: attributes rating, entity rating, title, description, media resources and template ID.
        """
        payload = {}
        
        # Parameter validation
        schema = FeedbackValidator.createReview()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.UpdateReviewRequest import UpdateReviewRequest
        schema = UpdateReviewRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["createReview"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["createReview"]).netloc, "post", await create_url_without_domain("/service/application/feedback/v1.0/review/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def updateReview(self, body=""):
        """Use this API to update customer reviews for a specific entity along with following data: attributes rating, entity rating, title, description, media resources and template ID.
        """
        payload = {}
        
        # Parameter validation
        schema = FeedbackValidator.updateReview()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.UpdateReviewRequest import UpdateReviewRequest
        schema = UpdateReviewRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["updateReview"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["updateReview"]).netloc, "put", await create_url_without_domain("/service/application/feedback/v1.0/review/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getReviews(self, entity_type=None, entity_id=None, id=None, user_id=None, media=None, rating=None, attribute_rating=None, facets=None, sort=None, active=None, approve=None, page_id=None, page_size=None, body=""):
        """Use this API to retrieve a list of customer reviews based on entity and filters provided.
        :param entity_type : Type of entity, e.g. product, delivery, seller, l3, order placed, order delivered, application, or template. : type string
        :param entity_id : ID of the eligible entity as specified in the entity type. : type string
        :param id : ID of the review. : type string
        :param user_id : ID of the user. : type string
        :param media : media type, e.g. image | video | video_file | video_link : type string
        :param rating : rating filter, e.g. 1-5 : type array
        :param attribute_rating : Filter for attribute rating. : type array
        :param facets : This is a boolean value for enabling metadata (facets). Selecting *true* will enable facets. : type boolean
        :param sort : Sort by: default | top | recent : type string
        :param active : Get the active reviews. : type boolean
        :param approve : Get the approved reviews. : type boolean
        :param page_id : Pagination page ID to retrieve next set of results. : type string
        :param page_size : The number of items to retrieve in each page. : type integer
        """
        payload = {}
        
        if entity_type:
            payload["entity_type"] = entity_type
        
        if entity_id:
            payload["entity_id"] = entity_id
        
        if id:
            payload["id"] = id
        
        if user_id:
            payload["user_id"] = user_id
        
        if media:
            payload["media"] = media
        
        if rating:
            payload["rating"] = rating
        
        if attribute_rating:
            payload["attribute_rating"] = attribute_rating
        
        if facets:
            payload["facets"] = facets
        
        if sort:
            payload["sort"] = sort
        
        if active:
            payload["active"] = active
        
        if approve:
            payload["approve"] = approve
        
        if page_id:
            payload["page_id"] = page_id
        
        if page_size:
            payload["page_size"] = page_size
        
        # Parameter validation
        schema = FeedbackValidator.getReviews()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getReviews"], proccessed_params="""{"required":[{"description":"Type of entity, e.g. product, delivery, seller, l3, order placed, order delivered, application, or template.","in":"path","name":"entity_type","required":true,"schema":{"type":"string"}},{"description":"ID of the eligible entity as specified in the entity type.","in":"path","name":"entity_id","required":true,"schema":{"type":"string"}}],"optional":[{"description":"ID of the review.","in":"query","name":"id","schema":{"type":"string"}},{"description":"ID of the user.","in":"query","name":"user_id","schema":{"type":"string"}},{"description":"media type, e.g. image | video | video_file | video_link","in":"query","name":"media","schema":{"type":"string"}},{"description":"rating filter, e.g. 1-5","explode":false,"in":"query","name":"rating","schema":{"items":{"type":"number"},"type":"array"},"style":"form"},{"description":"Filter for attribute rating.","explode":false,"in":"query","name":"attribute_rating","schema":{"items":{"type":"string"},"type":"array"},"style":"form"},{"description":"This is a boolean value for enabling metadata (facets). Selecting *true* will enable facets.","in":"query","name":"facets","schema":{"type":"boolean"}},{"description":"Sort by: default | top | recent","in":"query","name":"sort","schema":{"type":"string"}},{"description":"Get the active reviews.","in":"query","name":"active","schema":{"type":"boolean"}},{"description":"Get the approved reviews.","in":"query","name":"approve","schema":{"type":"boolean"}},{"description":"Pagination page ID to retrieve next set of results.","in":"query","name":"page_id","schema":{"type":"string"}},{"description":"The number of items to retrieve in each page.","in":"query","name":"page_size","schema":{"type":"integer"}}],"query":[{"description":"ID of the review.","in":"query","name":"id","schema":{"type":"string"}},{"description":"ID of the user.","in":"query","name":"user_id","schema":{"type":"string"}},{"description":"media type, e.g. image | video | video_file | video_link","in":"query","name":"media","schema":{"type":"string"}},{"description":"rating filter, e.g. 1-5","explode":false,"in":"query","name":"rating","schema":{"items":{"type":"number"},"type":"array"},"style":"form"},{"description":"Filter for attribute rating.","explode":false,"in":"query","name":"attribute_rating","schema":{"items":{"type":"string"},"type":"array"},"style":"form"},{"description":"This is a boolean value for enabling metadata (facets). Selecting *true* will enable facets.","in":"query","name":"facets","schema":{"type":"boolean"}},{"description":"Sort by: default | top | recent","in":"query","name":"sort","schema":{"type":"string"}},{"description":"Get the active reviews.","in":"query","name":"active","schema":{"type":"boolean"}},{"description":"Get the approved reviews.","in":"query","name":"approve","schema":{"type":"boolean"}},{"description":"Pagination page ID to retrieve next set of results.","in":"query","name":"page_id","schema":{"type":"string"}},{"description":"The number of items to retrieve in each page.","in":"query","name":"page_size","schema":{"type":"integer"}}],"headers":[],"path":[{"description":"Type of entity, e.g. product, delivery, seller, l3, order placed, order delivered, application, or template.","in":"path","name":"entity_type","required":true,"schema":{"type":"string"}},{"description":"ID of the eligible entity as specified in the entity type.","in":"path","name":"entity_id","required":true,"schema":{"type":"string"}}]}""", entity_type=entity_type, entity_id=entity_id, id=id, user_id=user_id, media=media, rating=rating, attribute_rating=attribute_rating, facets=facets, sort=sort, active=active, approve=approve, page_id=page_id, page_size=page_size)
        query_string = await create_query_string(entity_type=entity_type, entity_id=entity_id, id=id, user_id=user_id, media=media, rating=rating, attribute_rating=attribute_rating, facets=facets, sort=sort, active=active, approve=approve, page_id=page_id, page_size=page_size)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getReviews"]).netloc, "get", await create_url_without_domain("/service/application/feedback/v1.0/review/entity/{entity_type}/entity-id/{entity_id}", entity_type=entity_type, entity_id=entity_id, id=id, user_id=user_id, media=media, rating=rating, attribute_rating=attribute_rating, facets=facets, sort=sort, active=active, approve=approve, page_id=page_id, page_size=page_size), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getTemplates(self, template_id=None, entity_id=None, entity_type=None, body=""):
        """Use this API to retrieve the details of the following feedback template. order, delivered, application, seller, order, placed, product
        :param template_id : ID of the feedback template. : type string
        :param entity_id : ID of the eligible entity as specified in the entity type. : type string
        :param entity_type : Type of entity, e.g. product, delivery, seller, l3, order placed, order delivered, or application. : type string
        """
        payload = {}
        
        if template_id:
            payload["template_id"] = template_id
        
        if entity_id:
            payload["entity_id"] = entity_id
        
        if entity_type:
            payload["entity_type"] = entity_type
        
        # Parameter validation
        schema = FeedbackValidator.getTemplates()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getTemplates"], proccessed_params="""{"required":[],"optional":[{"description":"ID of the feedback template.","in":"query","name":"template_id","schema":{"type":"string"}},{"description":"ID of the eligible entity as specified in the entity type.","in":"query","name":"entity_id","schema":{"type":"string"}},{"description":"Type of entity, e.g. product, delivery, seller, l3, order placed, order delivered, or application.","in":"query","name":"entity_type","schema":{"type":"string"}}],"query":[{"description":"ID of the feedback template.","in":"query","name":"template_id","schema":{"type":"string"}},{"description":"ID of the eligible entity as specified in the entity type.","in":"query","name":"entity_id","schema":{"type":"string"}},{"description":"Type of entity, e.g. product, delivery, seller, l3, order placed, order delivered, or application.","in":"query","name":"entity_type","schema":{"type":"string"}}],"headers":[],"path":[]}""", template_id=template_id, entity_id=entity_id, entity_type=entity_type)
        query_string = await create_query_string(template_id=template_id, entity_id=entity_id, entity_type=entity_type)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getTemplates"]).netloc, "get", await create_url_without_domain("/service/application/feedback/v1.0/template/", template_id=template_id, entity_id=entity_id, entity_type=entity_type), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def createQuestion(self, body=""):
        """Use this API to create a new question with following data- tags, text, type, choices for MCQ type questions, maximum length of answer.
        """
        payload = {}
        
        # Parameter validation
        schema = FeedbackValidator.createQuestion()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.CreateQNARequest import CreateQNARequest
        schema = CreateQNARequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["createQuestion"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["createQuestion"]).netloc, "post", await create_url_without_domain("/service/application/feedback/v1.0/template/qna/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def updateQuestion(self, body=""):
        """Use this API to update the status of a question, its tags and its choices.
        """
        payload = {}
        
        # Parameter validation
        schema = FeedbackValidator.updateQuestion()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.UpdateQNARequest import UpdateQNARequest
        schema = UpdateQNARequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["updateQuestion"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["updateQuestion"]).netloc, "put", await create_url_without_domain("/service/application/feedback/v1.0/template/qna/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getQuestionAndAnswers(self, entity_type=None, entity_id=None, id=None, user_id=None, show_answer=None, page_id=None, page_size=None, body=""):
        """Use this API to retrieve a list of questions and answers for a given entity.
        :param entity_type : Type of entity, e.g. product, l3, etc. : type string
        :param entity_id : ID of the eligible entity as specified in the entity type. : type string
        :param id : QNA ID : type string
        :param user_id : User ID : type string
        :param show_answer : This is a boolean value. Select *true* to display answers given. : type boolean
        :param page_id : Pagination page ID to retrieve next set of results. : type string
        :param page_size : The number of items to retrieve in each page. : type integer
        """
        payload = {}
        
        if entity_type:
            payload["entity_type"] = entity_type
        
        if entity_id:
            payload["entity_id"] = entity_id
        
        if id:
            payload["id"] = id
        
        if user_id:
            payload["user_id"] = user_id
        
        if show_answer:
            payload["show_answer"] = show_answer
        
        if page_id:
            payload["page_id"] = page_id
        
        if page_size:
            payload["page_size"] = page_size
        
        # Parameter validation
        schema = FeedbackValidator.getQuestionAndAnswers()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getQuestionAndAnswers"], proccessed_params="""{"required":[{"description":"Type of entity, e.g. product, l3, etc.","in":"path","name":"entity_type","required":true,"schema":{"type":"string"}},{"description":"ID of the eligible entity as specified in the entity type.","in":"path","name":"entity_id","required":true,"schema":{"type":"string"}}],"optional":[{"description":"QNA ID","in":"query","name":"id","schema":{"type":"string"}},{"description":"User ID","in":"query","name":"user_id","schema":{"type":"string"}},{"description":"This is a boolean value. Select *true* to display answers given.","in":"query","name":"show_answer","schema":{"type":"boolean"}},{"description":"Pagination page ID to retrieve next set of results.","in":"query","name":"page_id","schema":{"type":"string"}},{"description":"The number of items to retrieve in each page.","in":"query","name":"page_size","schema":{"type":"integer"}}],"query":[{"description":"QNA ID","in":"query","name":"id","schema":{"type":"string"}},{"description":"User ID","in":"query","name":"user_id","schema":{"type":"string"}},{"description":"This is a boolean value. Select *true* to display answers given.","in":"query","name":"show_answer","schema":{"type":"boolean"}},{"description":"Pagination page ID to retrieve next set of results.","in":"query","name":"page_id","schema":{"type":"string"}},{"description":"The number of items to retrieve in each page.","in":"query","name":"page_size","schema":{"type":"integer"}}],"headers":[],"path":[{"description":"Type of entity, e.g. product, l3, etc.","in":"path","name":"entity_type","required":true,"schema":{"type":"string"}},{"description":"ID of the eligible entity as specified in the entity type.","in":"path","name":"entity_id","required":true,"schema":{"type":"string"}}]}""", entity_type=entity_type, entity_id=entity_id, id=id, user_id=user_id, show_answer=show_answer, page_id=page_id, page_size=page_size)
        query_string = await create_query_string(entity_type=entity_type, entity_id=entity_id, id=id, user_id=user_id, show_answer=show_answer, page_id=page_id, page_size=page_size)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getQuestionAndAnswers"]).netloc, "get", await create_url_without_domain("/service/application/feedback/v1.0/template/qna/entity/{entity_type}/entity-id/{entity_id}", entity_type=entity_type, entity_id=entity_id, id=id, user_id=user_id, show_answer=show_answer, page_id=page_id, page_size=page_size), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getVotes(self, id=None, ref_type=None, page_no=None, page_size=None, body=""):
        """Use this API to retrieve a list of votes of a current logged in user. Votes can be filtered using `ref_type`, i.e. review | comment.
        :param id : vote ID : type string
        :param ref_type : Entity type, e.g. review | comment. : type string
        :param page_no : The page number to navigate through the given set of results. Default value is 1. : type integer
        :param page_size : The number of items to retrieve in each page. : type integer
        """
        payload = {}
        
        if id:
            payload["id"] = id
        
        if ref_type:
            payload["ref_type"] = ref_type
        
        if page_no:
            payload["page_no"] = page_no
        
        if page_size:
            payload["page_size"] = page_size
        
        # Parameter validation
        schema = FeedbackValidator.getVotes()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getVotes"], proccessed_params="""{"required":[],"optional":[{"description":"vote ID","in":"query","name":"id","schema":{"type":"string"}},{"description":"Entity type, e.g. review | comment.","in":"query","name":"ref_type","schema":{"type":"string"}},{"description":"The page number to navigate through the given set of results. Default value is 1.","in":"query","name":"page_no","schema":{"type":"integer"}},{"description":"The number of items to retrieve in each page.","in":"query","name":"page_size","schema":{"type":"integer"}}],"query":[{"description":"vote ID","in":"query","name":"id","schema":{"type":"string"}},{"description":"Entity type, e.g. review | comment.","in":"query","name":"ref_type","schema":{"type":"string"}},{"description":"The page number to navigate through the given set of results. Default value is 1.","in":"query","name":"page_no","schema":{"type":"integer"}},{"description":"The number of items to retrieve in each page.","in":"query","name":"page_size","schema":{"type":"integer"}}],"headers":[],"path":[]}""", id=id, ref_type=ref_type, page_no=page_no, page_size=page_size)
        query_string = await create_query_string(id=id, ref_type=ref_type, page_no=page_no, page_size=page_size)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getVotes"]).netloc, "get", await create_url_without_domain("/service/application/feedback/v1.0/vote/", id=id, ref_type=ref_type, page_no=page_no, page_size=page_size), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def createVote(self, body=""):
        """Use this API to create a new vote, where the action could be an upvote or a downvote. This is useful when you want to give a vote (say upvote) to a review (ref_type) of a product (entity_type).
        """
        payload = {}
        
        # Parameter validation
        schema = FeedbackValidator.createVote()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.VoteRequest import VoteRequest
        schema = VoteRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["createVote"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["createVote"]).netloc, "post", await create_url_without_domain("/service/application/feedback/v1.0/vote/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def updateVote(self, body=""):
        """Use this API to update a vote with a new action, i.e. either an upvote or a downvote.
        """
        payload = {}
        
        # Parameter validation
        schema = FeedbackValidator.updateVote()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.UpdateVoteRequest import UpdateVoteRequest
        schema = UpdateVoteRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["updateVote"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["updateVote"]).netloc, "put", await create_url_without_domain("/service/application/feedback/v1.0/vote/", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    

class PosCart:
    def __init__(self, config):
        self._conf = config
        self._relativeUrls = {
            "getCart": "/service/application/pos/cart/v1.0/detail",
            "getCartLastModified": "/service/application/pos/cart/v1.0/detail",
            "addItems": "/service/application/pos/cart/v1.0/detail",
            "updateCart": "/service/application/pos/cart/v1.0/detail",
            "getItemCount": "/service/application/pos/cart/v1.0/basic",
            "getCoupons": "/service/application/pos/cart/v1.0/coupon",
            "applyCoupon": "/service/application/pos/cart/v1.0/coupon",
            "removeCoupon": "/service/application/pos/cart/v1.0/coupon",
            "getBulkDiscountOffers": "/service/application/pos/cart/v1.0/bulk-price",
            "applyRewardPoints": "/service/application/pos/cart/v1.0/redeem/points/",
            "getAddresses": "/service/application/pos/cart/v1.0/address",
            "addAddress": "/service/application/pos/cart/v1.0/address",
            "getAddressById": "/service/application/pos/cart/v1.0/address/{id}",
            "updateAddress": "/service/application/pos/cart/v1.0/address/{id}",
            "removeAddress": "/service/application/pos/cart/v1.0/address/{id}",
            "selectAddress": "/service/application/pos/cart/v1.0/select-address",
            "selectPaymentMode": "/service/application/pos/cart/v1.0/payment",
            "validateCouponForPayment": "/service/application/pos/cart/v1.0/payment/validate/",
            "getShipments": "/service/application/pos/cart/v1.0/shipment",
            "updateShipments": "/service/application/pos/cart/v1.0/shipment",
            "checkoutCart": "/service/application/pos/cart/v1.0/checkout",
            "updateCartMeta": "/service/application/pos/cart/v1.0/meta",
            "getAvailableDeliveryModes": "/service/application/pos/cart/v1.0/available-delivery-mode",
            "getStoreAddressByUid": "/service/application/pos/cart/v1.0/store-address",
            "getCartShareLink": "/service/application/pos/cart/v1.0/share-cart",
            "getCartSharedItems": "/service/application/pos/cart/v1.0/share-cart/{token}",
            "updateCartWithSharedItems": "/service/application/pos/cart/v1.0/share-cart/{token}/{action}"
            
        }
        self._urls = {
            method: f"{self._conf.domain}{path}" for method, path in self._relativeUrls.items()
        }

    async def updateUrls(self, urls):
        self._urls.update(urls)
    
    async def getCart(self, id=None, i=None, b=None, assign_card_id=None, body=""):
        """Use this API to get details of all the items added to a cart.
        :param id :  : type string
        :param i :  : type boolean
        :param b :  : type boolean
        :param assign_card_id :  : type integer
        """
        payload = {}
        
        if id:
            payload["id"] = id
        
        if i:
            payload["i"] = i
        
        if b:
            payload["b"] = b
        
        if assign_card_id:
            payload["assign_card_id"] = assign_card_id
        
        # Parameter validation
        schema = PosCartValidator.getCart()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getCart"], proccessed_params="""{"required":[],"optional":[{"in":"query","name":"id","schema":{"type":"string","description":"The unique identifier of the cart"}},{"in":"query","name":"i","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to retrieve all the items added in the cart."}},{"in":"query","name":"b","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to retrieve the price breakup of cart items."}},{"in":"query","name":"assign_card_id","schema":{"type":"integer","description":"Token of user's debit or credit card"}}],"query":[{"in":"query","name":"id","schema":{"type":"string","description":"The unique identifier of the cart"}},{"in":"query","name":"i","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to retrieve all the items added in the cart."}},{"in":"query","name":"b","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to retrieve the price breakup of cart items."}},{"in":"query","name":"assign_card_id","schema":{"type":"integer","description":"Token of user's debit or credit card"}}],"headers":[],"path":[]}""", id=id, i=i, b=b, assign_card_id=assign_card_id)
        query_string = await create_query_string(id=id, i=i, b=b, assign_card_id=assign_card_id)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getCart"]).netloc, "get", await create_url_without_domain("/service/application/pos/cart/v1.0/detail", id=id, i=i, b=b, assign_card_id=assign_card_id), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getCartLastModified(self, id=None, body=""):
        """Use this API to fetch Last-Modified timestamp in header metadata.
        :param id :  : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        
        # Parameter validation
        schema = PosCartValidator.getCartLastModified()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getCartLastModified"], proccessed_params="""{"required":[],"optional":[{"in":"query","name":"id","schema":{"type":"string","description":"The unique identifier of the cart"}}],"query":[{"in":"query","name":"id","schema":{"type":"string","description":"The unique identifier of the cart"}}],"headers":[],"path":[]}""", id=id)
        query_string = await create_query_string(id=id)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("HEAD", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getCartLastModified"]).netloc, "head", await create_url_without_domain("/service/application/pos/cart/v1.0/detail", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def addItems(self, i=None, b=None, body=""):
        """Use this API to add items to the cart.
        :param i :  : type boolean
        :param b :  : type boolean
        """
        payload = {}
        
        if i:
            payload["i"] = i
        
        if b:
            payload["b"] = b
        
        # Parameter validation
        schema = PosCartValidator.addItems()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.AddCartRequest import AddCartRequest
        schema = AddCartRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["addItems"], proccessed_params="""{"required":[],"optional":[{"in":"query","name":"i","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to retrieve all the items added in the cart."}},{"in":"query","name":"b","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to retrieve the price breakup of cart items."}}],"query":[{"in":"query","name":"i","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to retrieve all the items added in the cart."}},{"in":"query","name":"b","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to retrieve the price breakup of cart items."}}],"headers":[],"path":[]}""", i=i, b=b)
        query_string = await create_query_string(i=i, b=b)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["addItems"]).netloc, "post", await create_url_without_domain("/service/application/pos/cart/v1.0/detail", i=i, b=b), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def updateCart(self, id=None, i=None, b=None, body=""):
        """<p>Use this API to update items added to the cart with the help of a request object containing attributes like item_quantity and item_size. These attributes will be fetched from the following APIs</p> <ul> <li><font color="monochrome">operation</font> Operation for current api call. <b>update_item</b> for update items. <b>remove_item</b> for removing items.</li> <li> <font color="monochrome">item_id</font>  "/platform/content/v1/products/"</li> <li> <font color="monochrome">item_size</font>   "/platform/content/v1/products/:slug/sizes/"</li> <li> <font color="monochrome">quantity</font>  item quantity (must be greater than or equal to 1)</li> <li> <font color="monochrome">article_id</font>   "/content​/v1​/products​/:identifier​/sizes​/price​/"</li> <li> <font color="monochrome">item_index</font>  item position in the cart (must be greater than or equal to 0)</li> </ul>
        :param id :  : type string
        :param i :  : type boolean
        :param b :  : type boolean
        """
        payload = {}
        
        if id:
            payload["id"] = id
        
        if i:
            payload["i"] = i
        
        if b:
            payload["b"] = b
        
        # Parameter validation
        schema = PosCartValidator.updateCart()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.UpdateCartRequest import UpdateCartRequest
        schema = UpdateCartRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["updateCart"], proccessed_params="""{"required":[],"optional":[{"in":"query","name":"id","schema":{"type":"string","description":"The unique identifier of the cart"}},{"in":"query","name":"i","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to retrieve all the items added in the cart."}},{"in":"query","name":"b","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to retrieve the price breakup of cart items."}}],"query":[{"in":"query","name":"id","schema":{"type":"string","description":"The unique identifier of the cart"}},{"in":"query","name":"i","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to retrieve all the items added in the cart."}},{"in":"query","name":"b","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to retrieve the price breakup of cart items."}}],"headers":[],"path":[]}""", id=id, i=i, b=b)
        query_string = await create_query_string(id=id, i=i, b=b)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["updateCart"]).netloc, "put", await create_url_without_domain("/service/application/pos/cart/v1.0/detail", id=id, i=i, b=b), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getItemCount(self, id=None, body=""):
        """Use this API to get the total number of items present in cart.
        :param id : The unique identifier of the cart. : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        
        # Parameter validation
        schema = PosCartValidator.getItemCount()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getItemCount"], proccessed_params="""{"required":[],"optional":[{"name":"id","in":"query","description":"The unique identifier of the cart.","schema":{"type":"string"}}],"query":[{"name":"id","in":"query","description":"The unique identifier of the cart.","schema":{"type":"string"}}],"headers":[],"path":[]}""", id=id)
        query_string = await create_query_string(id=id)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getItemCount"]).netloc, "get", await create_url_without_domain("/service/application/pos/cart/v1.0/basic", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getCoupons(self, id=None, body=""):
        """Use this API to get a list of available coupons along with their details.
        :param id :  : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        
        # Parameter validation
        schema = PosCartValidator.getCoupons()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getCoupons"], proccessed_params="""{"required":[],"optional":[{"in":"query","name":"id","schema":{"type":"string","description":"The unique identifier of the cart."}}],"query":[{"in":"query","name":"id","schema":{"type":"string","description":"The unique identifier of the cart."}}],"headers":[],"path":[]}""", id=id)
        query_string = await create_query_string(id=id)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getCoupons"]).netloc, "get", await create_url_without_domain("/service/application/pos/cart/v1.0/coupon", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def applyCoupon(self, i=None, b=None, p=None, id=None, body=""):
        """Use this API to apply coupons on items in the cart.
        :param i :  : type boolean
        :param b :  : type boolean
        :param p :  : type boolean
        :param id :  : type string
        """
        payload = {}
        
        if i:
            payload["i"] = i
        
        if b:
            payload["b"] = b
        
        if p:
            payload["p"] = p
        
        if id:
            payload["id"] = id
        
        # Parameter validation
        schema = PosCartValidator.applyCoupon()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.ApplyCouponRequest import ApplyCouponRequest
        schema = ApplyCouponRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["applyCoupon"], proccessed_params="""{"required":[],"optional":[{"in":"query","name":"i","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to retrieve all the items added in the cart."}},{"in":"query","name":"b","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to retrieve the price breakup of cart items."}},{"in":"query","name":"p","schema":{"type":"boolean","description":"This is a boolean value. Select `true` for getting a payment option in response."}},{"in":"query","name":"id","schema":{"type":"string","description":"The unique identifier of the cart"}}],"query":[{"in":"query","name":"i","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to retrieve all the items added in the cart."}},{"in":"query","name":"b","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to retrieve the price breakup of cart items."}},{"in":"query","name":"p","schema":{"type":"boolean","description":"This is a boolean value. Select `true` for getting a payment option in response."}},{"in":"query","name":"id","schema":{"type":"string","description":"The unique identifier of the cart"}}],"headers":[],"path":[]}""", i=i, b=b, p=p, id=id)
        query_string = await create_query_string(i=i, b=b, p=p, id=id)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["applyCoupon"]).netloc, "post", await create_url_without_domain("/service/application/pos/cart/v1.0/coupon", i=i, b=b, p=p, id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def removeCoupon(self, id=None, body=""):
        """Remove Coupon applied on the cart by passing uid in request body.
        :param id : The unique identifier of the cart : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        
        # Parameter validation
        schema = PosCartValidator.removeCoupon()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["removeCoupon"], proccessed_params="""{"required":[],"optional":[{"name":"id","description":"The unique identifier of the cart","schema":{"type":"string"},"in":"query"}],"query":[{"name":"id","description":"The unique identifier of the cart","schema":{"type":"string"},"in":"query"}],"headers":[],"path":[]}""", id=id)
        query_string = await create_query_string(id=id)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["removeCoupon"]).netloc, "delete", await create_url_without_domain("/service/application/pos/cart/v1.0/coupon", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getBulkDiscountOffers(self, item_id=None, article_id=None, uid=None, slug=None, body=""):
        """Use this API to get a list of applicable offers along with current, next and best offer for given product. Either one of uid, item_id, slug should be present.
        :param item_id : The Item ID of the product : type integer
        :param article_id : Article Mongo ID : type string
        :param uid : UID of the product : type integer
        :param slug : A short, human-readable, URL-friendly identifier of a product. You can get slug value from the endpoint /service/application/catalog/v1.0/products/ : type string
        """
        payload = {}
        
        if item_id:
            payload["item_id"] = item_id
        
        if article_id:
            payload["article_id"] = article_id
        
        if uid:
            payload["uid"] = uid
        
        if slug:
            payload["slug"] = slug
        
        # Parameter validation
        schema = PosCartValidator.getBulkDiscountOffers()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getBulkDiscountOffers"], proccessed_params="""{"required":[],"optional":[{"name":"item_id","description":"The Item ID of the product","in":"query","schema":{"type":"integer"}},{"name":"article_id","description":"Article Mongo ID","in":"query","schema":{"type":"string"}},{"name":"uid","description":"UID of the product","in":"query","schema":{"type":"integer"}},{"name":"slug","description":"A short, human-readable, URL-friendly identifier of a product. You can get slug value from the endpoint /service/application/catalog/v1.0/products/","in":"query","schema":{"type":"string"}}],"query":[{"name":"item_id","description":"The Item ID of the product","in":"query","schema":{"type":"integer"}},{"name":"article_id","description":"Article Mongo ID","in":"query","schema":{"type":"string"}},{"name":"uid","description":"UID of the product","in":"query","schema":{"type":"integer"}},{"name":"slug","description":"A short, human-readable, URL-friendly identifier of a product. You can get slug value from the endpoint /service/application/catalog/v1.0/products/","in":"query","schema":{"type":"string"}}],"headers":[],"path":[]}""", item_id=item_id, article_id=article_id, uid=uid, slug=slug)
        query_string = await create_query_string(item_id=item_id, article_id=article_id, uid=uid, slug=slug)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getBulkDiscountOffers"]).netloc, "get", await create_url_without_domain("/service/application/pos/cart/v1.0/bulk-price", item_id=item_id, article_id=article_id, uid=uid, slug=slug), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def applyRewardPoints(self, id=None, i=None, b=None, body=""):
        """Use this API to redeem a fixed no. of reward points by applying it to the cart.
        :param id :  : type string
        :param i :  : type boolean
        :param b :  : type boolean
        """
        payload = {}
        
        if id:
            payload["id"] = id
        
        if i:
            payload["i"] = i
        
        if b:
            payload["b"] = b
        
        # Parameter validation
        schema = PosCartValidator.applyRewardPoints()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.RewardPointRequest import RewardPointRequest
        schema = RewardPointRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["applyRewardPoints"], proccessed_params="""{"required":[],"optional":[{"in":"query","name":"id","schema":{"type":"string","description":"The unique identifier of the cart"}},{"in":"query","name":"i","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to retrieve all the items added in the cart."}},{"in":"query","name":"b","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to retrieve the price breakup of cart items."}}],"query":[{"in":"query","name":"id","schema":{"type":"string","description":"The unique identifier of the cart"}},{"in":"query","name":"i","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to retrieve all the items added in the cart."}},{"in":"query","name":"b","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to retrieve the price breakup of cart items."}}],"headers":[],"path":[]}""", id=id, i=i, b=b)
        query_string = await create_query_string(id=id, i=i, b=b)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["applyRewardPoints"]).netloc, "post", await create_url_without_domain("/service/application/pos/cart/v1.0/redeem/points/", id=id, i=i, b=b), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getAddresses(self, cart_id=None, mobile_no=None, checkout_mode=None, tags=None, is_default=None, body=""):
        """Use this API to get all the addresses associated with an account. If successful, returns a Address resource in the response body specified in GetAddressesResponse.attibutes listed below are optional <ul> <li> <font color="monochrome">uid</font></li> <li> <font color="monochrome">address_id</font></li> <li> <font color="monochrome">mobile_no</font></li> <li> <font color="monochrome">checkout_mode</font></li> <li> <font color="monochrome">tags</font></li> <li> <font color="monochrome">default</font></li> </ul>
        :param cart_id :  : type string
        :param mobile_no :  : type string
        :param checkout_mode :  : type string
        :param tags :  : type string
        :param is_default :  : type boolean
        """
        payload = {}
        
        if cart_id:
            payload["cart_id"] = cart_id
        
        if mobile_no:
            payload["mobile_no"] = mobile_no
        
        if checkout_mode:
            payload["checkout_mode"] = checkout_mode
        
        if tags:
            payload["tags"] = tags
        
        if is_default:
            payload["is_default"] = is_default
        
        # Parameter validation
        schema = PosCartValidator.getAddresses()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getAddresses"], proccessed_params="""{"required":[],"optional":[{"name":"cart_id","in":"query","schema":{"type":"string","description":"The unique identifier of the cart"}},{"in":"query","name":"mobile_no","schema":{"type":"string","description":"10-digit mobile number"}},{"in":"query","name":"checkout_mode","schema":{"type":"string","description":"Option to checkout for self or for others"}},{"in":"query","name":"tags","schema":{"type":"string","description":"Tag given to an address, e.g. work, home, office, shop."}},{"in":"query","name":"is_default","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to fetch the default address."}}],"query":[{"name":"cart_id","in":"query","schema":{"type":"string","description":"The unique identifier of the cart"}},{"in":"query","name":"mobile_no","schema":{"type":"string","description":"10-digit mobile number"}},{"in":"query","name":"checkout_mode","schema":{"type":"string","description":"Option to checkout for self or for others"}},{"in":"query","name":"tags","schema":{"type":"string","description":"Tag given to an address, e.g. work, home, office, shop."}},{"in":"query","name":"is_default","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to fetch the default address."}}],"headers":[],"path":[]}""", cart_id=cart_id, mobile_no=mobile_no, checkout_mode=checkout_mode, tags=tags, is_default=is_default)
        query_string = await create_query_string(cart_id=cart_id, mobile_no=mobile_no, checkout_mode=checkout_mode, tags=tags, is_default=is_default)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getAddresses"]).netloc, "get", await create_url_without_domain("/service/application/pos/cart/v1.0/address", cart_id=cart_id, mobile_no=mobile_no, checkout_mode=checkout_mode, tags=tags, is_default=is_default), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def addAddress(self, body=""):
        """Use this API to add an address to an account.
        """
        payload = {}
        
        # Parameter validation
        schema = PosCartValidator.addAddress()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.Address import Address
        schema = Address()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["addAddress"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["addAddress"]).netloc, "post", await create_url_without_domain("/service/application/pos/cart/v1.0/address", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getAddressById(self, id=None, cart_id=None, mobile_no=None, checkout_mode=None, tags=None, is_default=None, body=""):
        """Use this API to get an addresses using its ID. If successful, returns a Address resource in the response body specified in `Address`. Attibutes listed below are optional <ul> <li> <font color="monochrome">mobile_no</font></li> <li> <font color="monochrome">checkout_mode</font></li> <li> <font color="monochrome">tags</font></li> <li> <font color="monochrome">default</font></li> </ul>
        :param id :  : type string
        :param cart_id :  : type string
        :param mobile_no :  : type string
        :param checkout_mode :  : type string
        :param tags :  : type string
        :param is_default :  : type boolean
        """
        payload = {}
        
        if id:
            payload["id"] = id
        
        if cart_id:
            payload["cart_id"] = cart_id
        
        if mobile_no:
            payload["mobile_no"] = mobile_no
        
        if checkout_mode:
            payload["checkout_mode"] = checkout_mode
        
        if tags:
            payload["tags"] = tags
        
        if is_default:
            payload["is_default"] = is_default
        
        # Parameter validation
        schema = PosCartValidator.getAddressById()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getAddressById"], proccessed_params="""{"required":[{"name":"id","in":"path","schema":{"type":"string","description":"ID allotted to the selected address"},"required":true}],"optional":[{"name":"cart_id","in":"query","schema":{"type":"string","description":"The unique identifier of the cart"}},{"in":"query","name":"mobile_no","schema":{"type":"string","description":"10-digit mobile number"}},{"in":"query","name":"checkout_mode","schema":{"type":"string","description":"Option to checkout for self or for others"}},{"in":"query","name":"tags","schema":{"type":"string","description":"Tag given to an address, e.g. work, home, office, shop."}},{"in":"query","name":"is_default","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to fetch the default address."}}],"query":[{"name":"cart_id","in":"query","schema":{"type":"string","description":"The unique identifier of the cart"}},{"in":"query","name":"mobile_no","schema":{"type":"string","description":"10-digit mobile number"}},{"in":"query","name":"checkout_mode","schema":{"type":"string","description":"Option to checkout for self or for others"}},{"in":"query","name":"tags","schema":{"type":"string","description":"Tag given to an address, e.g. work, home, office, shop."}},{"in":"query","name":"is_default","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to fetch the default address."}}],"headers":[],"path":[{"name":"id","in":"path","schema":{"type":"string","description":"ID allotted to the selected address"},"required":true}]}""", id=id, cart_id=cart_id, mobile_no=mobile_no, checkout_mode=checkout_mode, tags=tags, is_default=is_default)
        query_string = await create_query_string(id=id, cart_id=cart_id, mobile_no=mobile_no, checkout_mode=checkout_mode, tags=tags, is_default=is_default)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getAddressById"]).netloc, "get", await create_url_without_domain("/service/application/pos/cart/v1.0/address/{id}", id=id, cart_id=cart_id, mobile_no=mobile_no, checkout_mode=checkout_mode, tags=tags, is_default=is_default), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def updateAddress(self, id=None, body=""):
        """<p>Use this API to update an existing address in the account. Request object should contain attributes mentioned in  <font color="blue">Address </font> can be updated. These attributes are:</p> <ul> <li> <font color="monochrome">is_default_address</font></li> <li> <font color="monochrome">landmark</font></li> <li> <font color="monochrome">area</font></li> <li> <font color="monochrome">pincode</font></li> <li> <font color="monochrome">email</font></li> <li> <font color="monochrome">address_type</font></li> <li> <font color="monochrome">name</font></li> <li> <font color="monochrome">address_id</font></li> <li> <font color="monochrome">address</font></li> </ul>
        :param id : ID allotted to the selected address : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        
        # Parameter validation
        schema = PosCartValidator.updateAddress()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.Address import Address
        schema = Address()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["updateAddress"], proccessed_params="""{"required":[{"name":"id","description":"ID allotted to the selected address","schema":{"type":"string"},"in":"path","required":true}],"optional":[],"query":[],"headers":[],"path":[{"name":"id","description":"ID allotted to the selected address","schema":{"type":"string"},"in":"path","required":true}]}""", id=id)
        query_string = await create_query_string(id=id)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["updateAddress"]).netloc, "put", await create_url_without_domain("/service/application/pos/cart/v1.0/address/{id}", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def removeAddress(self, id=None, body=""):
        """Use this API to delete an address by its ID. This will returns an object that will indicate whether the address was deleted successfully or not.
        :param id : ID allotted to the selected address : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        
        # Parameter validation
        schema = PosCartValidator.removeAddress()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["removeAddress"], proccessed_params="""{"required":[{"name":"id","description":"ID allotted to the selected address","schema":{"type":"string"},"in":"path","required":true}],"optional":[],"query":[],"headers":[],"path":[{"name":"id","description":"ID allotted to the selected address","schema":{"type":"string"},"in":"path","required":true}]}""", id=id)
        query_string = await create_query_string(id=id)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("DELETE", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["removeAddress"]).netloc, "delete", await create_url_without_domain("/service/application/pos/cart/v1.0/address/{id}", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def selectAddress(self, cart_id=None, i=None, b=None, body=""):
        """<p>Select Address from all addresses associated with the account in order to ship the cart items to that address, otherwise default address will be selected implicitly. See `SelectCartAddressRequest` in schema of request body for the list of attributes needed to select Address from account. On successful request, this API returns a Cart object. Below address attributes are required. <ul> <li> <font color="monochrome">address_id</font></li> <li> <font color="monochrome">billing_address_id</font></li> <li> <font color="monochrome">uid</font></li> </ul></p>
        :param cart_id :  : type string
        :param i :  : type boolean
        :param b :  : type boolean
        """
        payload = {}
        
        if cart_id:
            payload["cart_id"] = cart_id
        
        if i:
            payload["i"] = i
        
        if b:
            payload["b"] = b
        
        # Parameter validation
        schema = PosCartValidator.selectAddress()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.SelectCartAddressRequest import SelectCartAddressRequest
        schema = SelectCartAddressRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["selectAddress"], proccessed_params="""{"required":[],"optional":[{"in":"query","name":"cart_id","schema":{"type":"string","description":"The unique identifier of the cart"}},{"in":"query","name":"i","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to retrieve all the items added in the cart."}},{"in":"query","name":"b","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to retrieve the price breakup of cart items."}}],"query":[{"in":"query","name":"cart_id","schema":{"type":"string","description":"The unique identifier of the cart"}},{"in":"query","name":"i","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to retrieve all the items added in the cart."}},{"in":"query","name":"b","schema":{"type":"boolean","description":"This is a boolean value. Select `true` to retrieve the price breakup of cart items."}}],"headers":[],"path":[]}""", cart_id=cart_id, i=i, b=b)
        query_string = await create_query_string(cart_id=cart_id, i=i, b=b)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["selectAddress"]).netloc, "post", await create_url_without_domain("/service/application/pos/cart/v1.0/select-address", cart_id=cart_id, i=i, b=b), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def selectPaymentMode(self, id=None, body=""):
        """Use this API to update cart payment.
        :param id :  : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        
        # Parameter validation
        schema = PosCartValidator.selectPaymentMode()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.UpdateCartPaymentRequest import UpdateCartPaymentRequest
        schema = UpdateCartPaymentRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["selectPaymentMode"], proccessed_params="""{"required":[],"optional":[{"in":"query","name":"id","schema":{"type":"string","description":"The unique identifier of the cart"}}],"query":[{"in":"query","name":"id","schema":{"type":"string","description":"The unique identifier of the cart"}}],"headers":[],"path":[]}""", id=id)
        query_string = await create_query_string(id=id)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["selectPaymentMode"]).netloc, "put", await create_url_without_domain("/service/application/pos/cart/v1.0/payment", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def validateCouponForPayment(self, id=None, address_id=None, payment_mode=None, payment_identifier=None, aggregator_name=None, merchant_code=None, body=""):
        """Use this API to validate a coupon against the payment mode such as NetBanking, Wallet, UPI etc.
        :param id :  : type string
        :param address_id :  : type string
        :param payment_mode :  : type string
        :param payment_identifier :  : type string
        :param aggregator_name :  : type string
        :param merchant_code :  : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        
        if address_id:
            payload["address_id"] = address_id
        
        if payment_mode:
            payload["payment_mode"] = payment_mode
        
        if payment_identifier:
            payload["payment_identifier"] = payment_identifier
        
        if aggregator_name:
            payload["aggregator_name"] = aggregator_name
        
        if merchant_code:
            payload["merchant_code"] = merchant_code
        
        # Parameter validation
        schema = PosCartValidator.validateCouponForPayment()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["validateCouponForPayment"], proccessed_params="""{"required":[],"optional":[{"in":"query","name":"id","schema":{"type":"string","description":"The unique identifier of the cart"}},{"in":"query","name":"address_id","schema":{"type":"string","description":"ID allotted to an address"}},{"in":"query","name":"payment_mode","schema":{"type":"string","description":"Payment mode selected by the customer"}},{"in":"query","name":"payment_identifier","schema":{"type":"string","description":"Identifier of payment like ICIC, PAYTM"}},{"in":"query","name":"aggregator_name","schema":{"type":"string","description":"Payment gateway identifier"}},{"in":"query","name":"merchant_code","schema":{"type":"string","description":"Identifier used by payment gateway for a given payment mode, e.g. NB_ICIC, PAYTM"}}],"query":[{"in":"query","name":"id","schema":{"type":"string","description":"The unique identifier of the cart"}},{"in":"query","name":"address_id","schema":{"type":"string","description":"ID allotted to an address"}},{"in":"query","name":"payment_mode","schema":{"type":"string","description":"Payment mode selected by the customer"}},{"in":"query","name":"payment_identifier","schema":{"type":"string","description":"Identifier of payment like ICIC, PAYTM"}},{"in":"query","name":"aggregator_name","schema":{"type":"string","description":"Payment gateway identifier"}},{"in":"query","name":"merchant_code","schema":{"type":"string","description":"Identifier used by payment gateway for a given payment mode, e.g. NB_ICIC, PAYTM"}}],"headers":[],"path":[]}""", id=id, address_id=address_id, payment_mode=payment_mode, payment_identifier=payment_identifier, aggregator_name=aggregator_name, merchant_code=merchant_code)
        query_string = await create_query_string(id=id, address_id=address_id, payment_mode=payment_mode, payment_identifier=payment_identifier, aggregator_name=aggregator_name, merchant_code=merchant_code)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["validateCouponForPayment"]).netloc, "get", await create_url_without_domain("/service/application/pos/cart/v1.0/payment/validate/", id=id, address_id=address_id, payment_mode=payment_mode, payment_identifier=payment_identifier, aggregator_name=aggregator_name, merchant_code=merchant_code), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getShipments(self, pick_at_store_uid=None, ordering_store_id=None, p=None, id=None, address_id=None, area_code=None, order_type=None, body=""):
        """Use this API to get shipment details, expected delivery date, items and price breakup of the shipment.
        :param pick_at_store_uid :  : type integer
        :param ordering_store_id :  : type integer
        :param p : This is a boolean value. Select `true` for getting a payment option in response. : type boolean
        :param id : The unique identifier of the cart : type string
        :param address_id : ID allotted to the selected address : type string
        :param area_code : The PIN Code of the destination address, e.g. 400059 : type string
        :param order_type : The order type of shipment HomeDelivery - If the customer wants the order home-delivered PickAtStore - If the customer wants the handover of an order at the store itself. : type string
        """
        payload = {}
        
        if pick_at_store_uid:
            payload["pick_at_store_uid"] = pick_at_store_uid
        
        if ordering_store_id:
            payload["ordering_store_id"] = ordering_store_id
        
        if p:
            payload["p"] = p
        
        if id:
            payload["id"] = id
        
        if address_id:
            payload["address_id"] = address_id
        
        if area_code:
            payload["area_code"] = area_code
        
        if order_type:
            payload["order_type"] = order_type
        
        # Parameter validation
        schema = PosCartValidator.getShipments()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getShipments"], proccessed_params="""{"required":[],"optional":[{"in":"query","name":"pick_at_store_uid","required":false,"schema":{"type":"integer","description":"ID of the store from where the order will be picked up by the customer, assuming the order_type is `PickAtStore`. This may or may not be the same as the ID of the ordering store."}},{"in":"query","name":"ordering_store_id","required":false,"schema":{"type":"integer","description":"ID of the store where the customer is ordering from."}},{"name":"p","description":"This is a boolean value. Select `true` for getting a payment option in response.","in":"query","schema":{"type":"boolean"}},{"name":"id","description":"The unique identifier of the cart","in":"query","schema":{"type":"string"}},{"name":"address_id","description":"ID allotted to the selected address","in":"query","schema":{"type":"string"}},{"name":"area_code","description":"The PIN Code of the destination address, e.g. 400059","in":"query","schema":{"type":"string"}},{"name":"order_type","description":"The order type of shipment HomeDelivery - If the customer wants the order home-delivered PickAtStore - If the customer wants the handover of an order at the store itself.","in":"query","schema":{"type":"string","enum":["HomeDelivery","PickAtStore"]}}],"query":[{"in":"query","name":"pick_at_store_uid","required":false,"schema":{"type":"integer","description":"ID of the store from where the order will be picked up by the customer, assuming the order_type is `PickAtStore`. This may or may not be the same as the ID of the ordering store."}},{"in":"query","name":"ordering_store_id","required":false,"schema":{"type":"integer","description":"ID of the store where the customer is ordering from."}},{"name":"p","description":"This is a boolean value. Select `true` for getting a payment option in response.","in":"query","schema":{"type":"boolean"}},{"name":"id","description":"The unique identifier of the cart","in":"query","schema":{"type":"string"}},{"name":"address_id","description":"ID allotted to the selected address","in":"query","schema":{"type":"string"}},{"name":"area_code","description":"The PIN Code of the destination address, e.g. 400059","in":"query","schema":{"type":"string"}},{"name":"order_type","description":"The order type of shipment HomeDelivery - If the customer wants the order home-delivered PickAtStore - If the customer wants the handover of an order at the store itself.","in":"query","schema":{"type":"string","enum":["HomeDelivery","PickAtStore"]}}],"headers":[],"path":[]}""", pick_at_store_uid=pick_at_store_uid, ordering_store_id=ordering_store_id, p=p, id=id, address_id=address_id, area_code=area_code, order_type=order_type)
        query_string = await create_query_string(pick_at_store_uid=pick_at_store_uid, ordering_store_id=ordering_store_id, p=p, id=id, address_id=address_id, area_code=area_code, order_type=order_type)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getShipments"]).netloc, "get", await create_url_without_domain("/service/application/pos/cart/v1.0/shipment", pick_at_store_uid=pick_at_store_uid, ordering_store_id=ordering_store_id, p=p, id=id, address_id=address_id, area_code=area_code, order_type=order_type), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def updateShipments(self, i=None, p=None, id=None, address_id=None, order_type=None, body=""):
        """Use this API to update the delivery type and quantity as per customer's preference for either store pick-up or home-delivery.
        :param i : This is a boolean value. Select `true` to retrieve all the items added in the cart. : type boolean
        :param p : This is a boolean value. Select `true` for getting a payment option in response. : type boolean
        :param id : The unique identifier of the cart : type string
        :param address_id : ID allotted to an address : type string
        :param order_type : The order type of shipment HomeDelivery - If the customer wants the order home-delivered PickAtStore - If the customer wants the handover of an order at the store itself. : type string
        """
        payload = {}
        
        if i:
            payload["i"] = i
        
        if p:
            payload["p"] = p
        
        if id:
            payload["id"] = id
        
        if address_id:
            payload["address_id"] = address_id
        
        if order_type:
            payload["order_type"] = order_type
        
        # Parameter validation
        schema = PosCartValidator.updateShipments()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.UpdateCartShipmentRequest import UpdateCartShipmentRequest
        schema = UpdateCartShipmentRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["updateShipments"], proccessed_params="""{"required":[],"optional":[{"name":"i","description":"This is a boolean value. Select `true` to retrieve all the items added in the cart.","in":"query","schema":{"type":"boolean"}},{"name":"p","description":"This is a boolean value. Select `true` for getting a payment option in response.","in":"query","schema":{"type":"boolean"}},{"name":"id","description":"The unique identifier of the cart","in":"query","schema":{"type":"string"}},{"name":"address_id","description":"ID allotted to an address","in":"query","schema":{"type":"string"}},{"name":"order_type","description":"The order type of shipment HomeDelivery - If the customer wants the order home-delivered PickAtStore - If the customer wants the handover of an order at the store itself.","in":"query","schema":{"type":"string"}}],"query":[{"name":"i","description":"This is a boolean value. Select `true` to retrieve all the items added in the cart.","in":"query","schema":{"type":"boolean"}},{"name":"p","description":"This is a boolean value. Select `true` for getting a payment option in response.","in":"query","schema":{"type":"boolean"}},{"name":"id","description":"The unique identifier of the cart","in":"query","schema":{"type":"string"}},{"name":"address_id","description":"ID allotted to an address","in":"query","schema":{"type":"string"}},{"name":"order_type","description":"The order type of shipment HomeDelivery - If the customer wants the order home-delivered PickAtStore - If the customer wants the handover of an order at the store itself.","in":"query","schema":{"type":"string"}}],"headers":[],"path":[]}""", i=i, p=p, id=id, address_id=address_id, order_type=order_type)
        query_string = await create_query_string(i=i, p=p, id=id, address_id=address_id, order_type=order_type)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["updateShipments"]).netloc, "put", await create_url_without_domain("/service/application/pos/cart/v1.0/shipment", i=i, p=p, id=id, address_id=address_id, order_type=order_type), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def checkoutCart(self, id=None, body=""):
        """Use this API to checkout all items in the cart for payment and order generation. For COD, order will be generated directly, whereas for other checkout modes, user will be redirected to a payment gateway.
        :param id :  : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        
        # Parameter validation
        schema = PosCartValidator.checkoutCart()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.CartPosCheckoutDetailRequest import CartPosCheckoutDetailRequest
        schema = CartPosCheckoutDetailRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["checkoutCart"], proccessed_params="""{"required":[],"optional":[{"in":"query","name":"id","required":false,"schema":{"type":"string","description":"The unique identifier of the cart"}}],"query":[{"in":"query","name":"id","required":false,"schema":{"type":"string","description":"The unique identifier of the cart"}}],"headers":[],"path":[]}""", id=id)
        query_string = await create_query_string(id=id)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["checkoutCart"]).netloc, "post", await create_url_without_domain("/service/application/pos/cart/v1.0/checkout", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def updateCartMeta(self, id=None, body=""):
        """Use this API to update cart meta like checkout_mode and gstin.
        :param id : The unique identifier of the cart : type string
        """
        payload = {}
        
        if id:
            payload["id"] = id
        
        # Parameter validation
        schema = PosCartValidator.updateCartMeta()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.CartMetaRequest import CartMetaRequest
        schema = CartMetaRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["updateCartMeta"], proccessed_params="""{"required":[],"optional":[{"name":"id","description":"The unique identifier of the cart","schema":{"type":"string"},"in":"query"}],"query":[{"name":"id","description":"The unique identifier of the cart","schema":{"type":"string"},"in":"query"}],"headers":[],"path":[]}""", id=id)
        query_string = await create_query_string(id=id)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("PUT", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["updateCartMeta"]).netloc, "put", await create_url_without_domain("/service/application/pos/cart/v1.0/meta", id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getAvailableDeliveryModes(self, area_code=None, id=None, body=""):
        """Use this API to get the delivery modes (home-delivery/store-pickup) along with a list of pickup stores available for a given cart at a given PIN Code. User can then view the address of a pickup store with the help of store-address API.
        :param area_code :  : type string
        :param id :  : type string
        """
        payload = {}
        
        if area_code:
            payload["area_code"] = area_code
        
        if id:
            payload["id"] = id
        
        # Parameter validation
        schema = PosCartValidator.getAvailableDeliveryModes()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getAvailableDeliveryModes"], proccessed_params="""{"required":[{"in":"query","name":"area_code","required":true,"schema":{"type":"string","description":"The PIN Code of the destination address, e.g. 400059"}}],"optional":[{"name":"id","in":"query","required":false,"schema":{"type":"string","description":"The unique identifier of the cart"}}],"query":[{"in":"query","name":"area_code","required":true,"schema":{"type":"string","description":"The PIN Code of the destination address, e.g. 400059"}},{"name":"id","in":"query","required":false,"schema":{"type":"string","description":"The unique identifier of the cart"}}],"headers":[],"path":[]}""", area_code=area_code, id=id)
        query_string = await create_query_string(area_code=area_code, id=id)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getAvailableDeliveryModes"]).netloc, "get", await create_url_without_domain("/service/application/pos/cart/v1.0/available-delivery-mode", area_code=area_code, id=id), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getStoreAddressByUid(self, store_uid=None, body=""):
        """Use this API to get the store details by entering the unique identifier of the pickup stores shown in the response of available-delivery-mode API.
        :param store_uid :  : type integer
        """
        payload = {}
        
        if store_uid:
            payload["store_uid"] = store_uid
        
        # Parameter validation
        schema = PosCartValidator.getStoreAddressByUid()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getStoreAddressByUid"], proccessed_params="""{"required":[{"in":"query","name":"store_uid","required":true,"schema":{"type":"integer","description":"The unique identifier of the store"}}],"optional":[],"query":[{"in":"query","name":"store_uid","required":true,"schema":{"type":"integer","description":"The unique identifier of the store"}}],"headers":[],"path":[]}""", store_uid=store_uid)
        query_string = await create_query_string(store_uid=store_uid)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getStoreAddressByUid"]).netloc, "get", await create_url_without_domain("/service/application/pos/cart/v1.0/store-address", store_uid=store_uid), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getCartShareLink(self, body=""):
        """Use this API to generate a shared cart snapshot and return a shortlink token. The link can be shared with other users for getting the same items in their cart.
        """
        payload = {}
        
        # Parameter validation
        schema = PosCartValidator.getCartShareLink()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.GetShareCartLinkRequest import GetShareCartLinkRequest
        schema = GetShareCartLinkRequest()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getCartShareLink"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getCartShareLink"]).netloc, "post", await create_url_without_domain("/service/application/pos/cart/v1.0/share-cart", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getCartSharedItems(self, token=None, body=""):
        """Use this API to get the shared cart details as per the token generated using the share-cart API.
        :param token : Token of the shared short link : type string
        """
        payload = {}
        
        if token:
            payload["token"] = token
        
        # Parameter validation
        schema = PosCartValidator.getCartSharedItems()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getCartSharedItems"], proccessed_params="""{"required":[{"name":"token","description":"Token of the shared short link","schema":{"type":"string"},"in":"path","required":true}],"optional":[],"query":[],"headers":[],"path":[{"name":"token","description":"Token of the shared short link","schema":{"type":"string"},"in":"path","required":true}]}""", token=token)
        query_string = await create_query_string(token=token)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getCartSharedItems"]).netloc, "get", await create_url_without_domain("/service/application/pos/cart/v1.0/share-cart/{token}", token=token), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def updateCartWithSharedItems(self, token=None, action=None, body=""):
        """Use this API to merge the shared cart with existing cart, or replace the existing cart with the shared cart. The `action` parameter is used to indicate the operation Merge or Replace.
        :param token : Token of the shared short link : type string
        :param action : Operation to perform on the existing cart merge or replace. : type string
        """
        payload = {}
        
        if token:
            payload["token"] = token
        
        if action:
            payload["action"] = action
        
        # Parameter validation
        schema = PosCartValidator.updateCartWithSharedItems()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["updateCartWithSharedItems"], proccessed_params="""{"required":[{"name":"token","description":"Token of the shared short link","schema":{"type":"string"},"in":"path","required":true},{"name":"action","description":"Operation to perform on the existing cart merge or replace.","schema":{"type":"string","enum":["merge","replace"]},"in":"path","required":true}],"optional":[],"query":[],"headers":[],"path":[{"name":"token","description":"Token of the shared short link","schema":{"type":"string"},"in":"path","required":true},{"name":"action","description":"Operation to perform on the existing cart merge or replace.","schema":{"type":"string","enum":["merge","replace"]},"in":"path","required":true}]}""", token=token, action=action)
        query_string = await create_query_string(token=token, action=action)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["updateCartWithSharedItems"]).netloc, "post", await create_url_without_domain("/service/application/pos/cart/v1.0/share-cart/{token}/{action}", token=token, action=action), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    

class Logistic:
    def __init__(self, config):
        self._conf = config
        self._relativeUrls = {
            "getTatProduct": "/service/application/logistics/v1.0",
            "getPincodeZones": "/service/application/logistics/v1.0/pincode/zones",
            "getPincodeCity": "/service/application/logistics/v1.0/pincode/{pincode}"
            
        }
        self._urls = {
            method: f"{self._conf.domain}{path}" for method, path in self._relativeUrls.items()
        }

    async def updateUrls(self, urls):
        self._urls.update(urls)
    
    async def getTatProduct(self, body=""):
        """Use this API to know the delivery turnaround time (TAT) by entering the product details along with the PIN Code of the location.
        """
        payload = {}
        
        # Parameter validation
        schema = LogisticValidator.getTatProduct()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.GetTatProductReqBody import GetTatProductReqBody
        schema = GetTatProductReqBody()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getTatProduct"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getTatProduct"]).netloc, "post", await create_url_without_domain("/service/application/logistics/v1.0", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getPincodeZones(self, body=""):
        """Get to know the zones of a specefic pincode
        """
        payload = {}
        
        # Parameter validation
        schema = LogisticValidator.getPincodeZones()
        schema.dump(schema.load(payload))
        
        # Body validation
        from .models.GetPincodeZonesReqBody import GetPincodeZonesReqBody
        schema = GetPincodeZonesReqBody()
        schema.dump(schema.load(body))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getPincodeZones"], proccessed_params="""{"required":[],"optional":[],"query":[],"headers":[],"path":[]}""", )
        query_string = await create_query_string()
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("POST", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getPincodeZones"]).netloc, "post", await create_url_without_domain("/service/application/logistics/v1.0/pincode/zones", ), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    
    async def getPincodeCity(self, pincode=None, body=""):
        """Use this API to retrieve a city by its PIN Code.
        :param pincode : The PIN Code of the area, e.g. 400059 : type string
        """
        payload = {}
        
        if pincode:
            payload["pincode"] = pincode
        
        # Parameter validation
        schema = LogisticValidator.getPincodeCity()
        schema.dump(schema.load(payload))
        

        url_with_params = await create_url_with_params(api_url=self._urls["getPincodeCity"], proccessed_params="""{"required":[{"name":"pincode","in":"path","description":"The PIN Code of the area, e.g. 400059","required":true,"schema":{"type":"string"}}],"optional":[],"query":[],"headers":[],"path":[{"name":"pincode","in":"path","description":"The PIN Code of the area, e.g. 400059","required":true,"schema":{"type":"string"}}]}""", pincode=pincode)
        query_string = await create_query_string(pincode=pincode)
        headers = {
            "Authorization": "Bearer " + base64.b64encode("{}:{}".format(self._conf.applicationID, self._conf.applicationToken).encode()).decode()
        }
        if self._conf.locationDetails:
            headers["x-location-detail"] = ujson.dumps(self._conf.locationDetails)
        for h in self._conf.extraHeaders:
            headers.update(h)
        exclude_headers = []
        for key, val in headers.items():
            if not key.startswith("x-fp-"):
                exclude_headers.append(key)
        return await AiohttpHelper().aiohttp_request("GET", url_with_params, headers=await get_headers_with_signature(urlparse(self._urls["getPincodeCity"]).netloc, "get", await create_url_without_domain("/service/application/logistics/v1.0/pincode/{pincode}", pincode=pincode), query_string, headers, body, exclude_headers=exclude_headers), data=body, cookies=self._conf.cookies)
    



class ApplicationClient:
    def __init__(self, config):
        self.config = config
        self.catalog = Catalog(config)
        self.cart = Cart(config)
        self.common = Common(config)
        self.lead = Lead(config)
        self.theme = Theme(config)
        self.user = User(config)
        self.content = Content(config)
        self.communication = Communication(config)
        self.share = Share(config)
        self.fileStorage = FileStorage(config)
        self.configuration = Configuration(config)
        self.payment = Payment(config)
        self.order = Order(config)
        self.rewards = Rewards(config)
        self.feedback = Feedback(config)
        self.posCart = PosCart(config)
        self.logistic = Logistic(config)
        

    async def setCookie(self, cookie):
        self.config.cookies = cookie

    async def setLocationDetails(self, locationDetails):
        schema = LocationValidator.validateLocationObj()
        schema.dump(schema.load(locationDetails))
        self.config.locationDetails = locationDetails

    async def setExtraHeaders(self, header):
        if header and type(header) == dict:
            self.config.extraHeaders.append(header)
        else:
            raise FDKClientValidationError("Context value should be an dict")
