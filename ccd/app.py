""" Main bootstrap and configuration module for pyccd.  Any module that
requires configuration or services should import app and obtain the
configuration or service from here.

app.py enables a very basic but sufficient form of loose coupling
by setting names of services & configuration once, then allowing other modules
that require these services/information to obtain them by name rather than
directly importing or instantiating.

Module level constructs are only evaluated once in a Python application's
lifecycle, usually at the time of first import. This pattern is borrowed
from Flask.
"""
import yaml, os, hashlib, zipfile


# Simplify parameter setting and make it easier for adjustment
class Parameters(dict):
    def __init__(self, config_path='parameters.yaml'):
        if '.zip' in config_path:
            zp, ym = config_path.split('.zip/')

            with zipfile.ZipFile('{}.zip'.format(zp), 'r') as myzip:
                with myzip.open(ym) as f:
                    conf = f.read()

        else:
            with open(config_path, 'r') as f:
                conf = f.read()

        super(Parameters, self).__init__(yaml.load(conf))

    def __getattr__(self, name):
        if name in self:
            return self[name]
        else:
            raise AttributeError('No such attribute: ' + name)

    def __setattr__(self, name, value):
        self[name] = value

    def __delattr__(self, name):
        if name in self:
            del self[name]
        else:
            raise AttributeError('No such attribute: ' + name)


# Don't need to be going down this rabbit hole just yet
# mainly here as reference
def numpy_hashkey(array):
    return hashlib.sha1(array).hexdigest()


# This is a string.fully.qualified.reference to the fitter function.
# Cannot import and supply the function directly or we'll get a
# circular dependency
FITTER_FN = 'ccd.models.lasso.fitted_model'


def get_default_params():
    return Parameters(os.path.join(os.path.dirname(__file__), 'parameters.yaml'))


def exreturn():
    """
    Provides an example ccd.detect return for downstream unit testing.

    Returns:
        example ccd.detect dict
    """
    return {'algorithm': 'lcmap-pyccd:2018.03.12',
            'change_models': [{'blue': {'coefficients': (0.04611813373097645,
                                                         284.43324176756244,
                                                         148.33361297977248,
                                                         13.613743283672978,
                                                         58.90215410153422,
                                                         1.8913492393251956,
                                                         25.08634422831887),
                                        'intercept': -32785.27578313946,
                                        'magnitude': 285.3788151400695,
                                        'rmse': 109.15086470799753},
                               'break_day': 727731,
                               'change_probability': 1.0,
                               'curve_qa': 8,
                               'end_day': 727715,
                               'green': {'coefficients': (0.04830502708409155,
                                                          296.5005821179507,
                                                          118.66854754123803,
                                                          28.300056259385535,
                                                          33.46311004772084,
                                                          17.639415933327008,
                                                          6.49683588729709),
                                         'intercept': -34142.93506659758,
                                         'magnitude': 346.5308234754375,
                                         'rmse': 124.08932566956867},
                               'nir': {'coefficients': (-0.06442643156672573,
                                                        -243.21882999207398,
                                                        -248.3089181280274,
                                                        121.89409190380161,
                                                        128.2325699396088,
                                                        -132.99625593826352,
                                                        68.19780152484304),
                                       'intercept': 48884.7828950372,
                                       'magnitude': 1030.1014581095624,
                                       'rmse': 293.18129074114563},
                               'observation_count': 65,
                               'red': {'coefficients': (0.08462234104996647,
                                                        542.8879956121976,
                                                        126.99572308853796,
                                                        71.85320197528704,
                                                        -33.94069251920876,
                                                        46.06505383938905,
                                                        -32.75118530187267),
                                       'intercept': -60316.502951858616,
                                       'magnitude': 466.49078733377246,
                                       'rmse': 151.32710230803997},
                               'start_day': 724419,
                               'swir1': {'coefficients': (0.07866278436294434,
                                                          232.77541499357451,
                                                          -154.40167432195548,
                                                          -110.19637492423497,
                                                          -249.8674808121493,
                                                          122.89071350663873,
                                                          -138.47541225010744),
                                         'intercept': -54674.00105068795,
                                         'magnitude': 1911.9877118456097,
                                         'rmse': 363.0782871749425},
                               'swir2': {'coefficients': (0.08577474887989744,
                                                          239.54847274758848,
                                                          38.32302482515981,
                                                          -120.67275997787898,
                                                          -259.4045946266856,
                                                          143.30132902022282,
                                                          -122.89557721586864),
                                         'intercept': -60635.33838778086,
                                         'magnitude': 1306.7197264916213,
                                         'rmse': 286.8749501319939},
                               'thermal': {'coefficients': (0.22300074252267127,
                                                            -1338.4909238273553,
                                                            -339.97662140777095,
                                                            361.8547617776643,
                                                            -262.4826940513475,
                                                            185.33437230556356,
                                                            -77.13221213940302),
                                           'intercept': -160403.11652078622,
                                           'magnitude': 1203.583717147354,
                                           'rmse': 406.77430812222497}},
                              {'blue': {'coefficients': (0.019118231134643896,
                                                         145.9770628389499,
                                                         171.47286506906383,
                                                         -15.431913562254266,
                                                         101.58159290248808,
                                                         12.874898705512754,
                                                         -1.5497810967282943),
                                        'intercept': -13526.159340794584,
                                        'magnitude': 400.28422723363565,
                                        'rmse': 102.97150889813369},
                               'break_day': 731419,
                               'change_probability': 1.0,
                               'curve_qa': 8,
                               'end_day': 731411,
                               'green': {'coefficients': (0.00023571972719498512,
                                                          74.49338296807949,
                                                          163.03752607937668,
                                                          -30.164900684131144,
                                                          74.26892788016649,
                                                          5.0618878754192345,
                                                          -9.118578826084011),
                                         'intercept': 255.74454880934505,
                                         'magnitude': 554.3319318875258,
                                         'rmse': 98.42322985107496},
                               'nir': {'coefficients': (-0.049873946037860654,
                                                        0.0,
                                                        134.91884081708815,
                                                        27.09612155010133,
                                                        79.3080661900623,
                                                        28.286218523240763,
                                                        -36.78374191371169),
                                       'intercept': 36832.42202567102,
                                       'magnitude': 1976.232373282597,
                                       'rmse': 163.8797815196773},
                               'observation_count': 76,
                               'red': {'coefficients': (-0.01812415092006969,
                                                        151.0917330052639,
                                                        221.21875547737298,
                                                        -40.009800827630464,
                                                        94.39684180040521,
                                                        3.923150486246046,
                                                        -10.756139516394557),
                                       'intercept': 13664.521345219508,
                                       'magnitude': 779.4094797297539,
                                       'rmse': 88.72612933825528},
                               'start_day': 728019,
                               'swir1': {'coefficients': (0.003118993394645434,
                                                          -84.91368000213582,
                                                          27.44453382184424,
                                                          -53.404204109749756,
                                                          -93.70156687087373,
                                                          53.48455541144598,
                                                          -36.817920053595195),
                                         'intercept': -2096.3884999557204,
                                         'magnitude': 2158.3477156771987,
                                         'rmse': 94.80270353881244},
                               'swir2': {'coefficients': (0.0033125603044071314,
                                                          -67.08032256487081,
                                                          51.55527846337562,
                                                          -38.76382825129303,
                                                          -69.9237851871376,
                                                          50.69512712594576,
                                                          -28.023465891651725),
                                         'intercept': -2275.678688184199,
                                         'magnitude': 1556.2946732323132,
                                         'rmse': 76.30297613802901},
                               'thermal': {'coefficients': (0.028490068254819537,
                                                            -1057.7695133961902,
                                                            -181.9806063278027,
                                                            0.0,
                                                            119.97720583164559,
                                                            -55.122034685005765,
                                                            120.02326816852957),
                                           'intercept': -19812.87806837732,
                                           'magnitude': 597.2910541031779,
                                           'rmse': 231.640206880215}},
                              {'blue': {'coefficients': (-0.06554197677698986,
                                                         358.6036670545938,
                                                         404.287599666018,
                                                         -69.9813672631287,
                                                         -10.052950507191225,
                                                         -103.43500823585407,
                                                         3.581175482462987),
                                        'intercept': 48987.8355113621,
                                        'magnitude': 261.2229780323687,
                                        'rmse': 108.27924964865709},
                               'break_day': 733883,
                               'change_probability': 1.0,
                               'curve_qa': 8,
                               'end_day': 733859,
                               'green': {'coefficients': (-0.09318775742836258,
                                                          319.1596414118276,
                                                          384.5036179247304,
                                                          -99.86420717835864,
                                                          -67.79999837845429,
                                                          -88.70422607989256,
                                                          19.146783595180597),
                                         'intercept': 69447.08070241715,
                                         'magnitude': 303.15642573536024,
                                         'rmse': 119.46002975529359},
                               'nir': {'coefficients': (-0.4291920378130277,
                                                        -145.95238812954148,
                                                        85.25725187716174,
                                                        11.711309734534707,
                                                        125.25081211703632,
                                                        -136.55905246907585,
                                                        -5.848645685732746),
                                       'intercept': 317034.4953729159,
                                       'magnitude': 664.354612696945,
                                       'rmse': 213.65671812568075},
                               'observation_count': 46,
                               'red': {'coefficients': (-0.18535491592252615,
                                                        437.17076038088226,
                                                        437.8810963465724,
                                                        -118.88652192106106,
                                                        -178.76397150126547,
                                                        -59.91042965417288,
                                                        19.269523705902287),
                                       'intercept': 137208.45910173818,
                                       'magnitude': 385.7368248433195,
                                       'rmse': 139.8267344409402},
                               'start_day': 732187,
                               'swir1': {'coefficients': (-0.3019664486960263,
                                                          263.58493919480105,
                                                          477.17234944527445,
                                                          -238.27289817438853,
                                                          -477.59733794308556,
                                                          14.06848675905922,
                                                          140.17348641434333),
                                         'intercept': 223886.84928889974,
                                         'magnitude': 1358.9295049543725,
                                         'rmse': 333.89529714244156},
                               'swir2': {'coefficients': (-0.20557064658133997,
                                                          196.2031163945631,
                                                          369.3991452149122,
                                                          -261.5749961152918,
                                                          -505.21149670251856,
                                                          1.4573656874414165,
                                                          47.69091116118103),
                                         'intercept': 152414.5061657034,
                                         'magnitude': 994.0361173288111,
                                         'rmse': 318.1901413347524},
                               'thermal': {'coefficients': (-0.2880076052764464,
                                                            -1664.7777513824124,
                                                            -301.64926063691235,
                                                            -59.98540893362974,
                                                            -161.75764283004165,
                                                            102.39031779794176,
                                                            7.504108895214555),
                                           'intercept': 212104.99138335788,
                                           'magnitude': 145.83636924953316,
                                           'rmse': 386.706871545373}},
                              {'blue': {'coefficients': (-0.16547353255401542,
                                                         92.5776889649161,
                                                         -0.0,
                                                         0.0,
                                                         -33.801056956719734,
                                                         -35.85945438579472,
                                                         2.8067582727968965),
                                        'intercept': 121850.85495380402,
                                        'magnitude': 64.92504330891097,
                                        'rmse': 45.59197653084766},
                               'break_day': 735011,
                               'change_probability': 1.0,
                               'curve_qa': 8,
                               'end_day': 734731,
                               'green': {'coefficients': (-0.38931755881191643,
                                                          170.69975272482648,
                                                          -18.68736583194331,
                                                          83.12569252735312,
                                                          -0.0,
                                                          -8.480897252042125,
                                                          28.702013363694828),
                                         'intercept': 286370.15767902764,
                                         'magnitude': 154.41785559459822,
                                         'rmse': 86.02493043029318},
                               'nir': {'coefficients': (-2.70866337151725,
                                                        0.0,
                                                        -327.0647865405419,
                                                        72.98317838828638,
                                                        89.81116596078105,
                                                        24.874804877616405,
                                                        -91.00319775026415),
                                       'intercept': 1989971.307931135,
                                       'magnitude': 1449.5275026765885,
                                       'rmse': 287.764258832229},
                               'observation_count': 35,
                               'red': {'coefficients': (-0.48930267576951053,
                                                        129.37025416813194,
                                                        -57.567466313291284,
                                                        0.0,
                                                        -102.29582771853475,
                                                        -36.15938932072732,
                                                        17.735751617309113),
                                       'intercept': 359742.1090917515,
                                       'magnitude': 235.86430644601933,
                                       'rmse': 115.03641655126606},
                               'start_day': 733939,
                               'swir1': {'coefficients': (-1.959196195793913,
                                                          239.63835806776405,
                                                          -85.86495126120583,
                                                          -62.75217085928084,
                                                          -0.0,
                                                          -65.17770238575595,
                                                          -6.128044892086824),
                                         'intercept': 1439241.716454551,
                                         'magnitude': 1273.3577348409453,
                                         'rmse': 169.60493130062156},
                               'swir2': {'coefficients': (-1.017256389568186,
                                                          200.93103899668944,
                                                          -11.6829874120418,
                                                          -0.0,
                                                          -2.628403525325887,
                                                          -48.87916633450982,
                                                          30.327759626559015),
                                         'intercept': 747364.6756594898,
                                         'magnitude': 660.2628908804618,
                                         'rmse': 120.85593079252116},
                               'thermal': {'coefficients': (-0.6965418465148505,
                                                            -1555.7684760087714,
                                                            -454.925773407087,
                                                            -164.4977291310571,
                                                            0.0,
                                                            -48.12325695271999,
                                                            24.189503552832733),
                                           'intercept': 512071.68787283154,
                                           'magnitude': 593.8690518476069,
                                           'rmse': 229.7046613954397}},
                              {'blue': {'coefficients': (0.013309239931112176,
                                                         208.4992307122923,
                                                         127.98488349230337,
                                                         0.0,
                                                         0.0,
                                                         0.0,
                                                         0.0),
                                        'intercept': -9374.293937157423,
                                        'magnitude': 0.0,
                                        'rmse': 159.83304245243963},
                               'break_day': 735515,
                               'change_probability': 0.0,
                               'curve_qa': 24,
                               'end_day': 735515,
                               'green': {'coefficients': (0.1471264049694959,
                                                          238.65109061636272,
                                                          200.65244716840164,
                                                          0.0,
                                                          0.0,
                                                          0.0,
                                                          0.0),
                                         'intercept': -107653.46246560094,
                                         'magnitude': 0.0,
                                         'rmse': 238.35392942729698},
                               'nir': {'coefficients': (0.4410389631136011,
                                                        -134.5007362661872,
                                                        -155.42612210792862,
                                                        0.0,
                                                        0.0,
                                                        0.0,
                                                        0.0),
                                       'intercept': -323832.35913922754,
                                       'magnitude': 0.0,
                                       'rmse': 255.80419165651813},
                               'observation_count': 23,
                               'red': {'coefficients': (0.14905354088434802,
                                                        273.65050055590183,
                                                        209.53007479625356,
                                                        0.0,
                                                        0.0,
                                                        0.0,
                                                        0.0),
                                       'intercept': -109083.96508958182,
                                       'magnitude': 0.0,
                                       'rmse': 215.1473451800292},
                               'start_day': 735011,
                               'swir1': {'coefficients': (0.1696000322196124,
                                                          4.990989401486709,
                                                          8.582448721102102,
                                                          0.0,
                                                          0.0,
                                                          0.0,
                                                          0.0),
                                         'intercept': -124458.1416108616,
                                         'magnitude': 0.0,
                                         'rmse': 88.84233081207732},
                               'swir2': {'coefficients': (0.08403177417250733,
                                                          16.007884608446158,
                                                          16.991722668251544,
                                                          0.0,
                                                          0.0,
                                                          0.0,
                                                          0.0),
                                         'intercept': -61612.78585861216,
                                         'magnitude': 0.0,
                                         'rmse': 57.1923577172125},
                               'thermal': {'coefficients': (0.20995700984704566,
                                                            -1555.7636271215479,
                                                            -441.3924816461445,
                                                            0.0,
                                                            0.0,
                                                            0.0,
                                                            0.0),
                                           'intercept': -153739.69086753431,
                                           'magnitude': 0.0,
                                           'rmse': 209.52353302591223}}],
            'cloud_prob': 0.26185101580135439,
            'processing_mask': [
            1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0,
            0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1,
            1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1,
            1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0,
            0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1,
            0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0,
            1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0,
            0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0,
            1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0,
            1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1,
            1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1,
            1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1,
            1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0],
            'snow_prob': 0.038708428760362568,
            'water_prob': 0.23153585450152681}
