from dataclasses import dataclass, field
from typing import Optional
import scrapy


@dataclass
class YellowpagesItem:
    name: Optional[str] = field(default=None)
    street_address: Optional[str] = field(default=None)
    address_locality: Optional[str] = field(default=None)
    address_region: Optional[str] = field(default=None)
    postal_code: Optional[str] = field(default=None)
    telephone: Optional[str] = field(default=None)
    website: Optional[str] = field(default=None)
    ratings: Optional[str] = field(default=None)
