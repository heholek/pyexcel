from functools import partial


class Plotter(object):
    def __init__(self, instance, **keywords):
        self._ref = instance
        self.__keywords = keywords

    def bar(self):
        file_type = 'echarts.html'
        memory_content = self._ref.save_to_memory(
            file_type, title=self._ref.name,
            mode='notebook', **self.__keywords)

        def get_content(self):
            return self.getvalue().decode('utf-8')

        setattr(memory_content,
                '_repr_html_',
                partial(get_content, memory_content))
        return memory_content

    def svg(self):
        file_type = 'svg'
        return self.__make_graphics(file_type)

    def jpeg(self):
        file_type = 'svg'
        return self.__make_graphics(file_type)

    def png(self):
        file_type = 'svg'
        return self.__make_graphics(file_type)

    def _repr_svg_(self):
        return self.svg()

    def __make_graphics(self, file_type):
        # make the signature for jypter notebook
        memory_content = self._ref.save_to_memory(
            file_type, **self.__keywords)

        def get_content(self):
            return self.getvalue().decode('utf-8')

        setattr(memory_content,
                '_repr_%s_' % file_type,
                partial(get_content, memory_content))
        return memory_content
