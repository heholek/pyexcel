import pyexcel as p


def test_bar():
    data = [['A', 'a', 'b', 'c', 'd'], ['z'], ['d']]
    s = p.get_sheet(array=data)
    s.name_columns_by_row(0)
    assert 'counts' in s.column.A.value_counts().plot.bar()._repr_html_()


def test_effectscatter():
    data = [{'x': 100, 'y': 200}, {'x': 1, 'y': 20}, {'x': 12, 'y': 30}]

    s = p.get_sheet(records=data)
    s.name_columns_by_row(0)
    assert 'echarts' in s.plot.effectscatter()._repr_html_()


def test_histogram():
    data = [[1, 2, 3, 4, 5, 5, 6, 9, 3, 4, 3]]
    sheet = p.get_sheet(array=data)
    sheet.transpose()
    assert 'histogram' in sheet.column[0].plot.hist()._repr_html_()


def test_wordcloud():
    data = [
        ['pyexcel', 310],
        ['django-excel', 110],
        ['Flask-excel', 90],
        ['pyexcel-io', 14],
    ]

    s = p.Sheet(data)
    assert 'wordcloud' in s.plot.wordcloud()._repr_html_()
