import numpy as np
import plotly.plotly as py
import plotly.graph_objs as go

from src.stats_test import run_permutation_test


# w6XMT6iHEc4Dnwnr4RB7
nb_uni = np.array([0.835, 0.805, 0.775, 0.84, 0.835, 0.8, 0.79, 0.815, 0.775, 0.845])
nb_bi = np.array([0.835, 0.81, 0.75, 0.84, 0.79, 0.795, 0.815, 0.8, 0.81, 0.84])
nb_both = np.array([0.855, 0.815, 0.785, 0.865, 0.825, 0.815, 0.8, 0.82, 0.785, 0.86])
svm_uni = np.array([0.86, 0.83, 0.8, 0.86, 0.8, 0.86, 0.82, 0.86, 0.83, 0.82])
svm_bi = np.array([0.77, 0.78, 0.8, 0.84, 0.84, 0.82, 0.82, 0.82, 0.81, 0.79])
svm_both = np.array([0.85, 0.84, 0.78, 0.88, 0.81, 0.85, 0.84, 0.86, 0.86, 0.84])
doc2vec_15 = np.array([81.5, 84.5, 83.5, 86.5, 80.0, 80.0, 84.0, 83.0, 86.5, 83.0]) / 100
doc2vec_18 = np.array([0.91, 0.875, 0.89, 0.93, 0.885, 0.875, 0.865, 0.905, 0.905, 0.895])
doc2vec_15_18 = np.array([0.83, 0.85, 0.845, 0.875, 0.81, 0.81, 0.84, 0.845, 0.875, 0.835])


def error_up(lst):
    return np.max(lst)-np.mean(lst)

def error_below(lst):
    return np.mean(lst)-np.min(lst)

def draw_bar_chart():
    
    trace1 = go.Bar(
        x=[
            np.mean(nb_uni),
            np.mean(nb_bi),
            np.mean(nb_both),
            np.mean(svm_uni),
            np.mean(svm_bi),
            np.mean(svm_both),
            np.mean(doc2vec_15),
            np.mean(doc2vec_18),
            np.mean(doc2vec_15_18)
        ][::-1],
        y=['NB-uni','NB-bi','NB-both','SVM-uni','SVM-bi','SVM-both','SVM-DM','SVM-DBOW','SVM-DM+DBOW'][::-1],
        width = [0.6,0.6,0.6,0.6,0.6,0.6,0.6,0.6,0.6],
        orientation='h',
        error_x=dict(
            type='data',
            color='rgb(240,131,91)',
            array=[
                error_up(nb_uni),
                error_up(nb_bi),
                error_up(nb_both),
                error_up(svm_uni),
                error_up(svm_bi),
                error_up(svm_both),
                error_up(doc2vec_15),
                error_up(doc2vec_18),
                error_up(doc2vec_15_18)
            ][::-1],
            arrayminus=[
                error_below(nb_uni),
                error_below(nb_bi),
                error_below(nb_both),
                error_below(svm_uni),
                error_below(svm_bi),
                error_below(svm_both),
                error_below(doc2vec_15),
                error_below(doc2vec_18),
                error_below(doc2vec_15_18)
            ][::-1],
            visible=True
        ),
        marker=dict(
            color=[
                'lightblue',
                'lightblue',
                'lightblue',
                'lightblue',
                'lightblue',
                'lightblue',
                'lightblue',
                'lightblue',
                'lightblue'
            ]
        ),
    )

    data = [trace1]
    layout=go.Layout(
        xaxis=dict(
            range=[0.75, 0.95],
            dtick=0.01
        ),
        font=dict(size=18),
        yaxis={'automargin': True}
    )
    fig = go.Figure(data=data, layout=layout)
    py.iplot(fig, filename='barchart')


RESULTS_NB_UNI = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1] 
# RESULTS_NB_UNI = [-1 if RESULTS_NB_UNI[i] == 0 else RESULTS_NB_UNI[i] for i in range(len(RESULTS_NB_UNI))]
RESULTS_NB_BI = [0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1]
# RESULTS_NB_BI = [-1 if RESULTS_NB_BI[i] == 0 else RESULTS_NB_BI[i] for i in range(len(RESULTS_NB_BI))]
RESULTS_NB_BOTH = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1]
# RESULTS_NB_BOTH = [-1 if RESULTS_NB_BOTH[i] == 0 else RESULTS_NB_BOTH[i] for i in range(len(RESULTS_NB_BOTH))]

RESULTS_SVM_UNI = "1. -1. -1. -1. -1. -1. -1. -1. -1. -1. -1. -1. -1. -1. -1. -1. -1.  1. -1. -1.  1. -1. -1. -1. -1. -1. -1.  1. -1.  1. -1. -1. -1. -1. -1.  1. -1.  1. -1. -1.  1. -1. -1. -1.  1. -1. -1. -1. -1. -1.  1.  1. -1. -1. -1. -1. -1. -1. -1. -1. -1. -1. -1. -1. -1. -1. -1.  1. -1. -1. -1. -1. -1.  1. -1. -1. -1.  1. -1.  1. -1. -1.  1.  1. -1. -1. -1. -1. -1. -1. -1. -1. -1. -1. -1.  1. -1. -1. -1. -1.  1.  1.  1.  1.  1.  1.  1. -1.  1.  1. -1. -1.  1.  1.  1.  1.  1.  1.  1. -1.  1.  1.  1.  1. -1. -1.  1.  1.  1.  1.  1.  1.  1.  1. -1.  1. -1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1. -1.  1.  1.  1.  1.  1. -1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1. -1.  1.  1. -1.  1.  1. -1.  1.  1.  1.  1.  1. -1.  1.  1. -1.  1.  1. -1.  1.  1. -1. -1.  1.  1.".split()
RESULTS_SVM_UNI = [int(float(x)) for x in RESULTS_SVM_UNI]
RESULTS_SVM_UNI = [0 if RESULTS_SVM_UNI[i] < 0 else RESULTS_SVM_UNI[i] for i in range(len(RESULTS_SVM_UNI))]
RESULTS_SVM_BI = "-1. -1. -1. -1. -1. -1. -1. -1. -1. -1. -1.  1. -1. -1.  1. -1. -1. -1. -1. -1. -1. -1. -1. -1. -1. -1. -1.  1. -1. -1.  1.  1. -1. -1. -1. -1. -1.  1. -1. -1. -1.  1. -1. -1.  1. -1. -1. -1. -1. -1. -1.  1.  1. -1. -1. -1. -1. -1. -1. -1. -1. -1. -1.  1. -1. -1. -1. -1. -1. -1. -1. -1. -1. -1. -1. -1. -1.  1. -1.  1. -1. -1.  1. -1.  1. -1. -1. -1. -1. -1.  1. -1. -1. -1. -1.  1. -1. -1. -1. -1.  1.  1.  1.  1.  1.  1.  1. -1.  1.  1. -1. -1.  1.  1.  1. -1.  1.  1. -1. -1.  1. -1.  1.  1.  1. -1.  1.  1.  1.  1.  1.  1.  1.  1. -1. -1. -1.  1.  1.  1. -1. -1.  1. -1.  1. -1.  1.  1.  1.  1.  1.  1.  1.  1.  1. -1.  1.  1.  1.  1.  1.  1.  1.  1. -1.  1.  1. -1.  1. -1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1. -1.  1.  1. -1.  1. -1.  1. -1.  1.  1.  1. -1. -1.  1.  1.  1.".split()
RESULTS_SVM_BI = [int(float(x)) for x in RESULTS_SVM_BI]
RESULTS_SVM_BI = [0 if RESULTS_SVM_BI[i] < 0 else RESULTS_SVM_BI[i] for i in range(len(RESULTS_SVM_BI))]
RESULTS_SVM_BOTH = "-1. -1. -1. -1. -1. -1. -1. -1. -1. -1. -1. -1. -1. -1. -1. -1. -1. -1. -1. -1. -1. -1. -1. -1. -1. -1. -1.  1. -1. -1. -1. -1. -1. -1. -1. -1. -1.  1. -1. -1.  1.  1. -1. -1.  1.  1. -1. -1. -1. -1.  1.  1. -1. -1. -1. -1. -1. -1. -1. -1. -1. -1. -1. -1. -1. -1. -1. -1. -1. -1. -1. -1. -1. -1. -1. -1. -1.  1. -1.  1. -1. -1.  1.  1. -1. -1. -1. -1. -1. -1. -1. -1. -1. -1. -1.  1. -1. -1. -1. -1.  1.  1.  1.  1.  1.  1.  1. -1. 1.  1. -1. -1.  1.  1.  1.  1.  1.  1. -1. -1.  1.  1.  1.  1.  1. -1. 1.  1.  1.  1.  1.  1.  1.  1. -1.  1. -1.  1.  1.  1.  1. -1.  1. -1. 1.  1.  1.  1.  1. -1.  1.  1.  1.  1.  1. -1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.  1. -1.  1.  1. -1.  1.  1.  1.  1.  1. -1.  1.  1. -1.  1.  1. -1.  1.  1. -1.  1. 1.  1.".split()
RESULTS_SVM_BOTH = [int(float(x)) for x in RESULTS_SVM_BOTH]
RESULTS_SVM_BOTH = [0 if RESULTS_SVM_BOTH[i] < 0 else RESULTS_SVM_BOTH[i] for i in range(len(RESULTS_SVM_BOTH))]

RESULTS_DM =[1.1182445, -2.5466168, -1.7382195, -1.1990983, -0.8410545, -1.860726, -0.36578309, -0.89527807, -1.8079039, -1.0150288, -2.1122858, -0.15530506, -2.3383331, -1.2837476, -0.35175225, -0.85680624, -1.2611748, -0.21102164, -0.83331221, -1.2180418, -1.31358, -0.82882625, -1.345518, -1.6708817, -1.9265689, -0.95541122, -3.5685207, 0.36681703, -1.765888, 0.57173888, -1.2451474, -0.60848765, -2.0027666, -1.8550626, -1.8068068, 0.082299523, -1.6354242, 0.49426697, -2.3944538, -1.2638878, -0.52154856, -0.12954207, -0.066776987, 0.07316982, 0.26552252, -1.0238347, -1.6789254, -1.9532113, -2.081916, -1.4704664, 0.33359575, -0.57932601, -2.0543715, -0.44709066, -1.1666916, -1.7333174, -1.968572, -0.66075465, -1.3009138, -2.509779, -0.83703995, -3.0229682, -0.74398152, -1.690964, -1.0220812, -1.1214811, -2.1310828, -0.20631074, -1.3624438, -1.1796192, -1.7542966, -0.14641323, -0.71921409, 0.86462384, 0.3509804, -0.94138166, -2.1556169, -0.75629253, -1.249853, 2.276362, -1.224191, 0.38163456, 1.0013955, -0.57422535, 0.17778993, -1.7196327, -1.0043891, -0.72731442, -0.78467101, -1.4028828, 1.1126069, -1.9059214, -1.7210087, -1.1947731, 0.73644305, -0.85894397, -0.82255352, -0.19545395, -2.1229809, -2.0862357, -0.125522, 0.33542202, 1.2328229, 2.4350032, 0.4683438, 1.4212054, 2.3725096, -1.2765775, -0.3617337, 0.75187508, -0.97210517, 1.0352041, 2.560149, 0.75032337, 1.3191245, 0.048792822, 2.7378035, 2.7127809, 1.1494975, -0.79988352, 1.6522449, 0.05737304, 0.95540642, 0.35527906, -0.10676404, 0.79768331, 0.25998843, 1.1091419, 3.0632651, 0.64701922, 1.5951553, 2.0813605, 2.2258408, 0.7164753, 0.783167, 1.2843251, 0.14406932, 3.6461438, 0.99851273, 2.2124283, -0.60545693, -0.68795416, 0.93207706, -1.799977, 1.1218423, 1.3410148, 1.7432089, 1.8401306, 0.82190393, 2.0492709, 1.1624987, -0.15726949, -0.1378309, 1.2361096, 1.6561142, -0.00075543976, 2.1625046, 1.9933969, -0.61803473, 1.1467395, 0.44585747, -0.35119647, 2.2436864, 1.9430658, 1.9927995, 1.7837472, 1.5594868, 0.28090781, 0.38044755, -0.62367284, 0.73917841, 0.88572165, -0.63469572, 1.4069855, 0.82345504, 1.2146673, 1.611825, 0.42807514, 0.26373537, 2.5293988, 0.66844252, 1.9969538, 2.3249455, 2.815106, 0.83088693, 1.3678974, 2.1751111, -0.68305378, 1.5333243, 1.1080227, -1.1078554, 1.584062, 0.94309444, 0.29034435, -0.1148886, 0.65518768, 0.92357509, 0.28823684, 1.8858651, 2.486281]
RESULTS_DM = [0 if RESULTS_DM[i] < 0 else 1 for i in range(len(RESULTS_DM))]
RESULTS_DBOW = [0.9939947, -1.2582591, -2.0313428, -1.1651666, -1.2388326, -1.6521843, -1.334231, -1.8690482, -1.1698742, -0.84924782, -2.3823246, -0.15368814, -2.7145418, -1.5096858, 0.31216527, -1.6520902, -0.81630699, -0.3171706, -2.0155891, -1.7430147, -0.44429336, -1.1999515, -2.0290846, -2.5999288, -1.9450971, -1.0705222, -2.9323777, -0.081619801, -2.6750672, -0.95516519, -1.1714651, -3.4374644, -0.97950791, -3.4689652, -1.9173292, -1.9425819, -1.8860798, -1.5179, -1.0230937, -2.943043, -0.33481333, -1.2747425, -0.76303235, -0.71350924, 0.23443536, -3.3543585, -1.0212841, -2.7728663, -2.5077441, -2.628994, -0.72912527, -0.41607782, -2.3307406, -1.1343269, -1.7038608, -1.4680539, -3.1267536, -1.9624291, -1.4477126, -2.0904363, -1.6896853, -2.4828051, -1.9259991, -2.1464586, -2.1350397, -0.97024291, -1.6828132, -1.0291257, -1.9932937, -1.636696, -0.94263657, -1.7863908, 1.1990789, -0.028741444, -0.82134807, -1.9086498, -2.5791393, -0.15374518, -2.851138, 0.53182557, -1.7053908, -1.5922854, 2.5817249, -1.780829, 0.4143895, -2.2823407, -1.1752123, -1.8285441, -0.87104308, -1.2943851, -1.1865186, -2.8929266, -2.2858063, -1.2354416, 0.49468686, -1.1163716, -1.4525559, -0.40193645, -3.8113268, -3.2632045, 1.1726485, 1.6035863, 0.41859107, 1.1343719, 2.1822373, 2.0059797, 0.85221023, -0.87068722, -0.37774691, 0.99671067, 0.73498612, -0.19355695, 1.7108347, 2.008949, 3.0169029, -1.2763983, 3.5361014, 4.5507257, 1.7702907, 1.1462311, 3.0739113, 0.98649941, 4.088004, 0.1787034, 1.0513754, 0.37237765, 0.8300552, 2.6521454, 3.5099106, 2.4002859, 1.8868848, 1.1853333, 2.7543296, 0.79344916, -0.075900999, 2.3927496, 0.60784704, 4.1315654, 2.4427924, 2.0484853, -0.41116765, 0.17824818, 0.77565609, -0.40027055, 1.7260087, 1.232305, 2.099791, 1.5248805, 1.147485, 1.963819, 2.3864124, 1.906643, 1.2800522, 1.6236266, 2.1561747, 0.079465038, 0.70319434, 1.144937, -0.20933364, 2.5200801, 1.6963323, -0.77417737, 1.9909825, 1.9459969, 1.9419492, 2.6159514, 2.3748577, 0.12417731, 1.1933807, -0.8205611, 0.28605532, 1.8496006, 0.87791667, 2.4033411, 2.228014, 0.32075208, 1.1039754, 2.2708099, 2.3662593, 2.4168041, 1.6396077, 1.565866, 4.3202652, 4.1989876, 2.8715039, 2.3180102, 2.1343965, -0.1651503, 1.1439111, 1.1275879, 0.82650718, 2.3463185, 1.9991479, -0.20697711, -0.074264581, 0.78393189, 0.61403338, 1.2765523, 3.1917756, 2.0989828]
RESULTS_DBOW = [0 if RESULTS_DBOW[i] < 0 else 1 for i in range(len(RESULTS_DBOW))]
RESULTS_DM_DBOW = [1.1227958, -2.4399321, -1.6887513, -1.188643, -0.79221217, -1.8004892, -0.37084792, -0.94296827, -1.7610859, -0.94227539, -2.1547039, -0.16063124, -2.3062384, -1.2381004, -0.32260287, -0.84088536, -1.132616, -0.14708221, -0.86511317, -1.2653557, -1.3143223, -0.83991999, -1.366897, -1.7399059, -1.9219034, -0.9139698, -3.5786599, 0.39736914, -1.7611674, 0.52027451, -1.2419998, -0.70726573, -1.9993117, -1.8983857, -1.8306569, 0.062834117, -1.5950865, 0.43763627, -2.3011798, -1.338243, -0.5168814, -0.15715491, -0.018505006, 0.1025346, 0.23150586, -1.112977, -1.6643373, -1.983633, -2.0805528, -1.5057795, 0.30388653, -0.56922515, -2.0306816, -0.46318924, -1.1524244, -1.7297432, -1.9483323, -0.66348832, -1.255783, -2.4793727, -0.80331953, -2.9842968, -0.79959359, -1.7079456, -1.0718321, -1.1593194, -2.1375668, -0.23429756, -1.3206628, -1.140193, -1.6555784, -0.15909847, -0.67699824, 0.83534822, 0.27756302, -0.91844387, -2.1237429, -0.73944801, -1.2700471, 2.1779411, -1.2295348, 0.31583096, 1.0783537, -0.54080195, 0.113703, -1.7231996, -0.98767891, -0.76499928, -0.77155057, -1.3739609, 1.076704, -1.972977, -1.7462703, -1.1983411, 0.71186576, -0.85039018, -0.8127405, -0.16579817, -2.1717991, -2.1181499, -0.073746719, 0.32559282, 1.1909755, 2.4343781, 0.54003176, 1.4212653, 2.3190608, -1.2163295, -0.40686505, 0.76375113, -0.88338227, 0.99041011, 2.524761, 0.80695593, 1.3698488, 0.06104424, 2.7317333, 2.6678506, 1.1226, -0.76297805, 1.6339703, 0.10302053, 1.0472923, 0.4063095, -0.070030829, 0.74584258, 0.33253456, 1.1952909, 3.1132636, 0.60583993, 1.6545931, 2.0097463, 2.2171858, 0.66712413, 0.74368035, 1.3132426, 0.10952949, 3.5917714, 1.0250973, 2.1984918, -0.64803816, -0.62242994, 0.97871269, -1.7283463, 1.1262485, 1.3275786, 1.7103925, 1.857756, 0.82075958, 2.0301552, 1.1611365, -0.11424012, -0.13830987, 1.2902403, 1.6306139, 0.10272137, 2.1107056, 1.9031836, -0.56401471, 1.181625, 0.44427428, -0.33807211, 2.2756743, 1.8906192, 2.0234761, 1.8386021, 1.5897888, 0.25944136, 0.39958528, -0.63167471, 0.73942895, 0.98121642, -0.61474815, 1.4801149, 0.83957759, 1.1503467, 1.5412262, 0.40501087, 0.34538183, 2.4648949, 0.68312943, 1.9443904, 2.359421, 2.7833808, 0.95960382, 1.3782584, 2.1514418, -0.65435757, 1.5406938, 1.10428, -1.0424718, 1.6056596, 0.98512701, 0.25110473, -0.10127489, 0.6743121, 0.92180681, 0.30386842, 1.9799636, 2.4526967]
RESULTS_DM_DBOW = [0 if RESULTS_DM_DBOW[i] < 0 else 1 for i in range(len(RESULTS_DM_DBOW))]


def pre_process_classification_results():
    # print(RESULTS_NB_UNI) 1
    # print(RESULTS_NB_BI) 2
    # print(RESULTS_NB_BOTH) 3
    # print(RESULTS_SVM_UNI) 4
    # print(RESULTS_SVM_BI) 5
    # print(RESULTS_SVM_BOTH) 6
    # print(RESULTS_DM) 7
    # print(RESULTS_DBOW) 8 
    # print(RESULTS_DM_DBOW) 9
    
    results = [
        RESULTS_NB_UNI, #1
        RESULTS_NB_BI, #2
        RESULTS_NB_BOTH, #3
        RESULTS_SVM_UNI, #4
        RESULTS_SVM_BI, #5
        RESULTS_SVM_BOTH, #6
        RESULTS_DM, #7
        RESULTS_DBOW, #8
        RESULTS_DM_DBOW, #9
        ]
    np.save("./results/classification", results)
    print("\nresults saved")


