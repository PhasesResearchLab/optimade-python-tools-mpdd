from .entries import ResourceMapper


__all__ = ("StructureMapper",)


class StructureMapper(ResourceMapper):

    ENDPOINT = "structures"
    ALIASES = (
        ("id", "task_id"),
        ("chemical_formula_descriptive", "pretty_formula"),
        ("chemical_formula_reduced", "pretty_formula"),
        ("chemical_formula_anonymous", "formula_anonymous"),
    )

    @classmethod
    def map_back(cls, doc: dict) -> dict:
        """Map properties from MongoDB to OPTiMaDe

        :param doc: A resource object in MongoDB format
        :type doc: dict

        :return: A resource object in OPTiMaDe format
        :rtype: dict
        """
        if "_id" in doc:
            del doc["_id"]
        if "nsites" not in doc:
            doc["nsites"] = len(doc.get("cartesian_site_positions", []))
        # print(doc)
        mapping = ((real, alias) for alias, real in cls.all_aliases())
        newdoc = {}
        reals = {real for alias, real in cls.all_aliases()}
        for k in doc:
            if k not in reals:
                newdoc[k] = doc[k]
        for real, alias in mapping:
            if real in doc:
                newdoc[alias] = doc[real]

        # print(newdoc)
        if "attributes" in newdoc:
            raise Exception("Will overwrite doc field!")
        newdoc["attributes"] = newdoc.copy()
        for k in {"id", "type"}:
            newdoc["attributes"].pop(k, None)
        for k in list(newdoc.keys()):
            if k not in ("id", "attributes"):
                del newdoc[k]
        newdoc["type"] = cls.ENDPOINT
        return newdoc
