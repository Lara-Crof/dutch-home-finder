from enum import Enum


class HouseStatus(str, Enum):
    SOLD = "sold"
    RECENTLY_PUBLISHED = "recently_published"
    OLD_PUBLISHED = "old_published"
    DONT_KNOW = "dont_know"


class HouseCondition(str, Enum):
    NEW = "new"
    GOOD = "good"
    RENOVATED = "renovated"
    NEEDS_RENOVATION = "needs_renovation"


class PropertyType(str, Enum):
    APARTMENT = "apartment"
    HOUSE = "house"
    STUDIO = "studio"
    VILLA = "villa"
    ROW_HOUSE = "row_house"
    SEMI_DETACHED = "semi_detached"
    DETACHED = "detached"
