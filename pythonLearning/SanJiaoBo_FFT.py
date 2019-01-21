# -*- coding: gbk -*-
from enthought.traits.api import \
    Str, Float, HasTraits, Property, cached_property, Range, Instance, on_trait_change, Enum

from enthought.chaco.api import Plot, AbstractPlotData, ArrayPlotData, VPlotContainer

from enthought.traits.ui.api import \
    Item, View, VGroup, HSplit, ScrubberEditor, VSplit

from enthought.enable.api import Component, ComponentEditor
from enthought.chaco.tools.api import PanTool, ZoomTool

import numpy as np

# ����϶��޸�ֵ�Ŀؼ�����ʽ
scrubber = ScrubberEditor(
    hover_color  = 0xFFFFFF,
    active_color = 0xA0CD9E,
    border_color = 0x808080
)

# ȡFFT����Ľ��freqs�е�ǰn����кϳɣ����غϳɽ��������loops�����ڵĲ���
def fft_combine(freqs, n, loops=1):
    length = len(freqs) * loops
    data = np.zeros(length)
    index = loops * np.arange(0, length, 1.0) / length * (2 * np.pi)
    for k, p in enumerate(freqs[:n]):
        if k != 0: p *= 2 # ��ȥֱ���ɷ�֮�⣬�����ϵ����*2
        data += np.real(p) * np.cos(k*index) # ���ҳɷֵ�ϵ��Ϊʵ����
        data -= np.imag(p) * np.sin(k*index) # ���ҳɷֵ�ϵ��Ϊ����������
    return index, data

class TriangleWave(HasTraits):
    # ָ�����ǲ�����խ�����Χ������Range�ƺ����ܽ�������traits������
    # ���Զ��������������trait����
    low = Float(0.02)
    hi = Float(1.0)

    # ���ǲ��εĿ��
    wave_width = Range("low", "hi", 0.5)

    # ���ǲ��Ķ���C��x������
    length_c = Range("low", "wave_width", 0.5)

    # ���ǲ��Ķ����y������
    height_c = Float(1.0)

    # FFT������ʹ�õ�ȡ��������������һ��Enum���͵������Թ��û����б���ѡ��
    fftsize = Enum( [(2**x) for x in range(6, 12)])

    # FFTƵ��ͼ��x������ֵ
    fft_graph_up_limit = Range(0, 400, 20)

    # ������ʾFFT�Ľ��
    peak_list = Str

    # ���ö��ٸ�Ƶ�ʺϳ����ǲ�
    N = Range(1, 40, 4)

    # �����ͼ���ݵĶ���
    plot_data = Instance(AbstractPlotData)

    # ���Ʋ���ͼ������
    plot_wave = Instance(Component)

    # ����FFTƵ��ͼ������
    plot_fft  = Instance(Component)

    # ����������ͼ������
    container = Instance(Component)

    # �����û��������ͼ�� ע��һ��Ҫָ�����ڵĴ�С��������ͼ��������������ʼ��
    view = View(
        HSplit(
            VSplit(
                VGroup(
                    Item("wave_width", editor = scrubber, label=u"���ο��"),
                    Item("length_c", editor = scrubber, label=u"��ߵ�x����"),
                    Item("height_c", editor = scrubber, label=u"��ߵ�y����"),
                    Item("fft_graph_up_limit", editor = scrubber, label=u"Ƶ��ͼ��Χ"),
                    Item("fftsize", label=u"FFT����"),
                    Item("N", label=u"�ϳɲ�Ƶ����")
                ),
                Item("peak_list", style="custom", show_label=False, width=100, height=250)
            ),
            VGroup(
                Item("container", editor=ComponentEditor(size=(600,300)), show_label = False),
                orientation = "vertical"
            )
        ),
        resizable = True,
        width = 800,
        height = 600,
        title = u"���ǲ�FFT��ʾ"
    )

    # ������ͼ�ĸ�����������������ͼ��Ƶ��ͼ�кܶ����Ƶĵط�����˵�����һ��������
    # �����ظ�����
    def _create_plot(self, data, name, type="line"):
        p = Plot(self.plot_data)
        p.plot(data, name=name, title=name, type=type)
        p.tools.append(PanTool(p))
        zoom = ZoomTool(component=p, tool_mode="box", always_on=False)
        p.overlays.append(zoom)
        p.title = name
        return p

    def __init__(self):
        # ������Ҫ���ø���ĳ�ʼ������
        super(TriangleWave, self).__init__()

        # ������ͼ���ݼ�����ʱû��������˶���ֵΪ�գ�ֻ�Ǵ����������֣��Թ�Plot����
        self.plot_data = ArrayPlotData(x=[], y=[], f=[], p=[], x2=[], y2=[])

        # ����һ����ֱ���еĻ�ͼ����������Ƶ��ͼ�Ͳ���ͼ��������
        self.container = VPlotContainer()

        # ��������ͼ������ͼ�����������ߣ� ԭʼ����(x,y)�ͺϳɲ���(x2,y2)
        self.plot_wave = self._create_plot(("x","y"), "Triangle Wave")
        self.plot_wave.plot(("x2","y2"), color="red")

        # ����Ƶ��ͼ��ʹ�����ݼ��е�f��p
        self.plot_fft  = self._create_plot(("f","p"), "FFT", type="scatter")

        # ��������ͼ������ӵ���ֱ������
        self.container.add( self.plot_wave )
        self.container.add( self.plot_fft )

        # ����
        self.plot_wave.x_axis.title = "Samples"
        self.plot_fft.x_axis.title = "Frequency pins"
        self.plot_fft.y_axis.title = "(dB)"

        # �ı�fftsizeΪ1024����ΪEnum��Ĭ��ȱʡֵΪö���б��еĵ�һ��ֵ
        self.fftsize = 1024

    # FFTƵ��ͼ��x������ֵ�ĸı��¼��������������µ�ֵ��ֵ��Ƶ��ͼ����Ӧ����
    def _fft_graph_up_limit_changed(self):
        self.plot_fft.x_axis.mapper.range.high = self.fft_graph_up_limit

    def _N_changed(self):
        self.plot_sin_combine()

    # ���trait���Եĸı��¼���������ͬʱ��������@on_trait_changeָ��
    @on_trait_change("wave_width, length_c, height_c, fftsize")
    def update_plot(self):
        # �������ǲ�
        global y_data
        x_data = np.arange(0, 1.0, 1.0/self.fftsize)
        func = self.triangle_func()
        # ��func�����ķ���ֵǿ��ת����float64
        y_data = np.cast["float64"](func(x_data))

        # ����Ƶ��
        fft_parameters = np.fft.fft(y_data) / len(y_data)

        # �������Ƶ�ʵ����
        fft_data = np.clip(20*np.log10(np.abs(fft_parameters))[:self.fftsize/2+1], -120, 120)

        # ������Ľ��д�����ݼ�
        self.plot_data.set_data("x", np.arange(0, self.fftsize)) # x����Ϊȡ����
        self.plot_data.set_data("y", y_data)
        self.plot_data.set_data("f", np.arange(0, len(fft_data))) # x����ΪƵ�ʱ��
        self.plot_data.set_data("p", fft_data)

        # �ϳɲ���x����Ϊȡ���㣬��ʾ2������
        self.plot_data.set_data("x2", np.arange(0, 2*self.fftsize))

        # ����Ƶ��ͼx������
        self._fft_graph_up_limit_changed()

        # ���������-80dB��Ƶ�����
        peak_index = (fft_data > -80)
        peak_value = fft_data[peak_index][:20]
        result = []
        for f, v in zip(np.flatnonzero(peak_index), peak_value):
            result.append("%s : %s" %(f, v) )
        self.peak_list = "\n".join(result)

        # �������ڵ�fft�����������������Һϳɲ�
        self.fft_parameters = fft_parameters
        self.plot_sin_combine()

    # �������Һϳɲ�������2������
    def plot_sin_combine(self):
        index, data = fft_combine(self.fft_parameters, self.N, 2)
        self.plot_data.set_data("y2", data)

    # ����һ��ufunc����ָ�����������ǲ�
    def triangle_func(self):
        c = self.wave_width
        c0 = self.length_c
        hc = self.height_c

        def trifunc(x):
            x = x - int(x) # ���ǲ�������Ϊ1�����ֻȡx�����С�����ֽ��м���
            if x >= c: r = 0.0
            elif x < c0: r = x / c0 * hc
            else: r = (c-x) / (c-c0) * hc
            return r

        # ��trifunc��������һ��ufunc����������ֱ�Ӷ�������м���, ����ͨ���˺���
        # ����õ�����һ��Object���飬��Ҫ��������ת��
        return np.frompyfunc(trifunc, 1, 1)

if __name__ == "__main__":
    triangle = TriangleWave()
    triangle.configure_traits()