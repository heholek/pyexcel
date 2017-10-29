import pyexcel as p


def test_bar():
    data = [
        ['A', 'a', 'b', 'c', 'd'],
        ['z'],
        ['d']
    ]
    s = p.get_sheet(array=data)
    s.name_columns_by_row(0)
    assert 'counts' in s.column.A.value_counts().plot().bar()._repr_html_()


def test_effectscatter():
    data = [
        {
            'x': 100,
            'y': 200
        },
        {
            'x': 1,
            'y': 20
        },
        {
            'x': 12,
            'y': 30
        }
    ]

    s = p.get_sheet(records=data)
    s.name_columns_by_row(0)
    assert 'echarts' in s.plot().effectscatter()._repr_html_()
