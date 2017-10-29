from functools import partial


class Plotter(object):
    def __init__(self, instance):
        self._ref = instance

    def bar(self, **keywords):
        chart_type = 'bar'
        return self.__make_echarts_html(chart_type, **keywords)

    def bar3d(self, **keywords):
        chart_type = 'bar3d'
        return self.__make_echarts_html(chart_type, **keywords)

    def effectscatter(self, **keywords):
        chart_type = 'effectscatter'
        return self.__make_echarts_html(chart_type, **keywords)

    def scatter(self, **keywords):
        chart_type = 'scatter'
        return self.__make_echarts_html(chart_type, **keywords)

    def __make_echarts_html(self, chart_type, **keywords):
        file_type = 'echarts.html'
        memory_content = self._ref.save_to_memory(
            file_type, title=self._ref.name, chart_type=chart_type,
            mode='notebook', **keywords)

        def get_content(self):
            return self.getvalue().decode('utf-8')

        setattr(memory_content,
                '_repr_html_',
                partial(get_content, memory_content))
        return memory_content

    def svg(self, **keywords):
        file_type = 'svg'
        return self.__make_graphics(file_type, **keywords)

    def jpeg(self, **keywords):
        file_type = 'svg'
        return self.__make_graphics(file_type, **keywords)

    def png(self, **keywords):
        file_type = 'svg'
        return self.__make_graphics(file_type)

    def _repr_svg_(self):
        return self.svg()

    def __make_graphics(self, file_type, **keywords):
        # make the signature for jypter notebook
        memory_content = self._ref.save_to_memory(
            file_type, **keywords)

        def get_content(self):
            return self.getvalue().decode('utf-8')

        setattr(memory_content,
                '_repr_%s_' % file_type,
                partial(get_content, memory_content))
        return memory_content
