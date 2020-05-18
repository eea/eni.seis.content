from eni.seis.content.interfaces import INationalReport
from itertools import groupby
from plone.dexterity.content import Container
from zope.interface import implementer


@implementer(INationalReport)
class NationalReport(Container):
    """ National Report content type """

    def get_view_url(self):
        """ Return its external link if exists or absolute_url
            (because in some cases a report can act like a page with links or
            some other content)
        """
        if self.has_external_link():
            return self.external_link
        return self.absolute_url()

    def has_external_link(self):
        """ Return True if it has a link, else False
        """
        if self.external_link:
            return True
        return False

    def has_file(self):
        """ Return True if it has a file, else False
        """
        if self.file:
            return True
        return False

    def grouped_coverage(self, years):
        """ Given an iterable of numbers, group them by range
        """
        def extract_years(data):
            """
                2003-2006 -> [2003, 2004, 2005, 2006]
                2000 -> [2000]
                abc -> invalid: abc
            """
            result = []
            invalid = False
            try:
                year = int(data)
                result.append(year)
                return result
            except ValueError:
                try:
                    years = data.split("-")
                    if len(years) == 2:
                        start = int(years[0])
                        end = int(years[1]) + 1
                        for year in range(start, end):
                            result.append(year)
                        return result
                    else:
                        invalid = True
                except Exception:
                    return "invalid: " + data

            if invalid is True:
                return "invalid: " + data

        data = []
        for item in years:
            temp = extract_years(item)
            if "invalid" not in temp:
                for x in temp:
                    data.append(x)

        # [TODO] In this moment data contains the list of all years. Use this
        # as search filter later.

        source = [int(x) for x in sorted(set(data))]
        output = []

        def group_func(idx_nr):
            """ Used as comparator for grouping
            """
            index, number = idx_nr
            return index - number

        for _key, group in groupby(enumerate(source), group_func):
            result = [x[1] for x in group]

            if len(result) == 1:
                output.append("{0}".format(result[0]))
            else:
                output.append("{0}-{1}".format(result[0], result[-1]))

        return output

    def human_readable_years(self):
        return self.grouped_coverage(self.years)
