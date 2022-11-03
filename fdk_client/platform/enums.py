"""Platform Enums."""

from enum import Enum




class PriorityEnum(Enum):
    
    LOW = "low"
    
    MEDIUM = "medium"
    
    HIGH = "high"
    
    URGENT = "urgent"
    
    @classmethod
    async def is_valid(cls, value):
        if value in cls._value2member_map_:
            return None
        raise Exception("Invalid PriorityEnum type")


class HistoryTypeEnum(Enum):
    
    RATING = "rating"
    
    LOG = "log"
    
    COMMENT = "comment"
    
    @classmethod
    async def is_valid(cls, value):
        if value in cls._value2member_map_:
            return None
        raise Exception("Invalid HistoryTypeEnum type")


class TicketAssetTypeEnum(Enum):
    
    IMAGE = "image"
    
    VIDEO = "video"
    
    FILE = "file"
    
    YOUTUBE = "youtube"
    
    PRODUCT = "product"
    
    COLLECTION = "collection"
    
    BRAND = "brand"
    
    SHIPMENT = "shipment"
    
    ORDER = "order"
    
    @classmethod
    async def is_valid(cls, value):
        if value in cls._value2member_map_:
            return None
        raise Exception("Invalid TicketAssetTypeEnum type")


class TicketSourceEnum(Enum):
    
    PLATFORM_PANEL = "platform_panel"
    
    SALES_CHANNEL = "sales_channel"
    
    @classmethod
    async def is_valid(cls, value):
        if value in cls._value2member_map_:
            return None
        raise Exception("Invalid TicketSourceEnum type")





class PageType(Enum):
    
    ABOUT_US = "about-us"
    
    ADDRESSES = "addresses"
    
    BLOG = "blog"
    
    BRANDS = "brands"
    
    CARDS = "cards"
    
    CART = "cart"
    
    CATEGORIES = "categories"
    
    BRAND = "brand"
    
    CATEGORY = "category"
    
    COLLECTION = "collection"
    
    COLLECTIONS = "collections"
    
    CONTACT_US = "contact-us"
    
    EXTERNAL = "external"
    
    FAQ = "faq"
    
    FRESHCHAT = "freshchat"
    
    HOME = "home"
    
    NOTIFICATION_SETTINGS = "notification-settings"
    
    ORDERS = "orders"
    
    PAGE = "page"
    
    POLICY = "policy"
    
    PRODUCT = "product"
    
    PRODUCT_REVIEWS = "product-reviews"
    
    ADD_PRODUCT_REVIEW = "add-product-review"
    
    PRODUCT_REQUEST = "product-request"
    
    PRODUCTS = "products"
    
    PROFILE = "profile"
    
    PROFILE_BASIC = "profile-basic"
    
    PROFILE_COMPANY = "profile-company"
    
    PROFILE_EMAILS = "profile-emails"
    
    PROFILE_PHONES = "profile-phones"
    
    RATE_US = "rate-us"
    
    REFER_EARN = "refer-earn"
    
    SETTINGS = "settings"
    
    SHARED_CART = "shared-cart"
    
    TNC = "tnc"
    
    TRACK_ORDER = "track-order"
    
    WISHLIST = "wishlist"
    
    SECTIONS = "sections"
    
    FORM = "form"
    
    CART_DELIVERY = "cart-delivery"
    
    CART_PAYMENT = "cart-payment"
    
    CART_REVIEW = "cart-review"
    
    LOGIN = "login"
    
    REGISTER = "register"
    
    SHIPPING_POLICY = "shipping-policy"
    
    RETURN_POLICY = "return-policy"
    
    @classmethod
    async def is_valid(cls, value):
        if value in cls._value2member_map_:
            return None
        raise Exception("Invalid PageType type")


















class SubscriberStatus(Enum):
    
    ACTIVE = "active"
    
    INACTIVE = "inactive"
    
    BLOCKED = "blocked"
    
    @classmethod
    async def is_valid(cls, value):
        if value in cls._value2member_map_:
            return None
        raise Exception("Invalid SubscriberStatus type")



