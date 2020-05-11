import datajoint as dj


class Atlas(dj.Lookup):
    definition = """
    atlas           : varchar(32)
    ---
    atlas_desc=''   : varchar(255)
    """

class BrainRegion(dj.Manual):
    definition = """
    -> Atlas
    acronym                 : varchar(36)
    ---
    brain_region_name       : varchar(36)
    brain_region_desc=''    : varchar(1024)
    """


class ParentRegion(dj.Lookup):
    definition = """
    -> BrainRegion
    ---
    -> BrainRegion.proj(parent='acronym')
    """


class Point(dj.Imported):
    definition = """
    -> Atlas
    x: decimal(6,2)   # (µm)
    y: decimal(6,2)   # (µm)
    z: decimal(6,2)   # (µm)
    ---
    -> BrainRegion
    """

    def get_regions(self, key):
        pass
