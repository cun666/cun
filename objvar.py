# -*- coding: utf-8 -*- 
from Demos.winprocess import out

param_dict = {
    'IN0-EN' : '1',
    'IN0-SCCB_IDX' : '1',
    'IN0-SDS_EN' : '1',
    'IN0-SENSOR0-SET_INDEX' : '0',
    'IN0-SENSOR1-SET_INDEX' : '1',
    'IN0-SENSOR0-LANE_NUM' : '4',
    'IN0-SENSOR1-LANE_NUM' : '4',
    
    'OUT0-SENSOR1-LANE_NUM' : '4',
}

class SENSOR_CFG(object):
    def __init__(self):
        self.set_index = 0
        self.lane_num = 2
        
    def __str__(self):
        return "set_index {}, lane_num {}".format(self.set_index, self.lane_num)

class INPUT_CFG(object):
    def __init__(self):
        self.sensor = {}
        self.en = 0
        self.sccb_idx = 0
        self.sds_en = 0
    
    def __str__(self):
        return "en {}, sensor {}, sccb_idx {}, sds_en {}".format(self.en, self.sensor, self.sccb_idx, self.sds_en)
        
class EMBL_CFG(object):
    def __init__(self):
        self.en = 0
        self.preovi = {}
        self.postovi = {}
        
    def __str__(self):
        return "en {} preovi {}, postovi {}".format(self.en, self.preovi, self.postovi)
        
class OUTPUT_CFG(object):
    def __init__(self):
        self.embl = EMBL_CFG()
        self.en = 0
        self.rtmode = 0
        
    def __str__(self):
        return "en {}, rtmode {}, embl {}".format(self.en, self.rtmode, self.embl)
        
class SDSTXPORT_CFG(object):
    def __init__(self):
        self.en = 0
        self.vcmap = {}
        
    def __str__(self):
        return "en {}, vcmap {}".format(self.en, self.vcmap)
        
class SERDES_CFG(object):
    def __init__(self):
        self.txport = SDSTXPORT_CFG()
        
    def __str__(self):
        return "txport {}".format(self.txport)


class APP_TOP(object):
    def __init__(self):
        self.in0 = INPUT_CFG()
        self.out0 = OUTPUT_CFG()
        self.serdes = SERDES_CFG()
        
    def __str__(self):
        return "in0 {}, out0 {}, serdes {}".format(self.in0, self.out0, self.serdes)