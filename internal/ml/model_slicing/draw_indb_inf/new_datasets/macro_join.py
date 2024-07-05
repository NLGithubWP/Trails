import json
from matplotlib.ticker import FuncFormatter


def thousands_formatter(x, pos):
    if x >= 1e3:
        return '{:.1f}k'.format(x * 1e-3)
    else:
        return '{:.1f}'.format(x)


thousands_format = FuncFormatter(thousands_formatter)

from config import *

bar_width = 0.2  # Adjust bar width for better fit
spacing = bar_width / 2  # Adjust spacing to ensure symmetry


# Helper function to load data
def load_data(filepath):
    with open(filepath, 'r') as file:
        return json.load(file)


def scale_to_ms(latencies):
    result = {}
    for key, value in latencies.items():
        value = value * 1000
        result[key] = value
    return result


# here run 10k rows for inference.,
# each sub-list is "compute time" and "data fetch time"
datasets_result = {

    # Hcdr datasets
    'Credit': {
        'out_db_wo_join': {'load_model': 0.08953046798706055, 'data_query_time': 2.8702762126922607,
                           'py_conver_to_tensor': 0.42409825325012207, 'tensor_to_gpu': 8.630752563476562e-05,
                           'py_compute': 0.3413412570953369, 'overall_query_latency': 3.934831380844116},
        'in_db_wo_join': {'mem_allocate_time': 0.046573999, 'data_query_time_spi': 0.343235082,
                          'python_compute_time': 0.501055263, 'model_init_time': 0.009541483,
                          'overall_query_latency': 2.195732048, 'diff': -0.046581859999999864,
                          'data_type_convert_time': 1.247244199, 'data_query_time': 1.638553442,
                          'py_conver_to_tensor': 0.014708757400512695, 'py_compute': 0.39806079864501953,
                          'py_overall_duration': 0.42017054557800293, 'py_diff': 0.007400989532470703},
        'out_db_join': {'load_model': 0.0923161506652832, 'data_query_time': 3.1957552433013916,
                        'py_conver_to_tensor': 0.3607821464538574, 'tensor_to_gpu': 6.580352783203125e-05,
                        'py_compute': 0.2959768772125244, 'overall_query_latency': 4.151448488235474},
        'in_db_join': {'model_init_time': 0.009772562, 'data_type_convert_time': 1.186813152,
                       'data_query_time': 2.589222349, 'python_compute_time': 0.449734902,
                       'overall_query_latency': 3.078992093, 'diff': -0.030262280000000086,
                       'mem_allocate_time': 0.030250188, 'data_query_time_spi': 1.3818609099999999,
                       'py_conver_to_tensor': 0.014644145965576172, 'py_compute': 0.38569045066833496,
                       'py_overall_duration': 0.40750551223754883, 'py_diff': 0.007170915603637695},
    },

    # Diabetes dataset
    'Diabetes': {

        'out_db_wo_join': {'load_model': 0.1039266586303711, 'data_query_time': 2.0870604515075684,
                           'py_conver_to_tensor': 0.28963255882263184, 'tensor_to_gpu': 7.176399230957031e-05,
                           'py_compute': 0.285736083984375, 'overall_query_latency': 2.8772103786468506},

        'in_db_wo_join': {'mem_allocate_time': 0.027362219, 'model_init_time': 0.010055741,
                          'data_query_time_spi': 0.166548796, 'data_query_time': 1.029582073,
                          'python_compute_time': 0.487216135, 'overall_query_latency': 1.554225487,
                          'data_type_convert_time': 0.841480709, 'diff': -0.02737153800000014,
                          'py_conver_to_tensor': 0.01747870445251465, 'py_compute': 0.42203354835510254,
                          'py_overall_duration': 0.45314645767211914, 'py_diff': 0.013634204864501953},

        'out_db_join': {'load_model': 0.09507131576538086, 'data_query_time': 2.5441927909851074,
                        'py_conver_to_tensor': 0.3214762210845947, 'tensor_to_gpu': 0.00013637542724609375,
                        'py_compute': 0.2979896068572998, 'overall_query_latency': 3.4009222984313965},

        'in_db_join': {'diff': -0.02079015999999978, 'model_init_time': 0.009885554,
                       'data_type_convert_time': 0.83870191, 'data_query_time': 2.320049377,
                       'mem_allocate_time': 0.020779264, 'python_compute_time': 0.512643846,
                       'overall_query_latency': 2.8633689369999997, 'data_query_time_spi': 1.452491238,
                       'py_conver_to_tensor': 0.01607990264892578, 'py_compute': 0.4545469284057617,
                       'py_overall_duration': 0.4778456687927246, 'py_diff': 0.007218837738037109},
    },
}

datasets = list(datasets_result.keys())

# Plotting
fig, ax = plt.subplots(figsize=(6.4, 4.5))

# Initial flags to determine whether the labels have been set before
set_label_in_db_data_query = True
set_label_in_db_data_copy_start_py = True
set_label_in_db_data_preprocess = True
set_label_in_db_data_compute = True
set_label_in_db_data_others = True
set_label_in_db_model_load = True

indices = []
index = 0
speed_up_list = []

for dataset, valuedic in datasets_result.items():
    indices.append(index)

    out_db_wo_join = scale_to_ms(valuedic["out_db_wo_join"])
    in_db_wo_join = scale_to_ms(valuedic["in_db_wo_join"])
    out_db_join = scale_to_ms(valuedic["out_db_join"])
    in_db_join = scale_to_ms(valuedic["in_db_join"])

    speed_up_list.append([dataset, in_db_join["overall_query_latency"], out_db_join["overall_query_latency"]])

    # set labesl
    label_in_db_model_load = 'Model Loading' if set_label_in_db_model_load else None
    label_in_db_data_query = 'Data Retrieval' if set_label_in_db_data_query else None
    label_in_db_data_copy_start_py = 'Data Copying' if set_label_in_db_data_copy_start_py else None
    label_in_db_data_preprocess = 'Data Preprocessing' if set_label_in_db_data_preprocess else None
    label_in_db_data_compute = 'Inference' if set_label_in_db_data_compute else None
    label_in_db_data_others = 'Others' if set_label_in_db_data_others else None

    model_load_default = in_db_join["model_init_time"]

    # with join
    out_db_data_query = out_db_wo_join["data_query_time"]
    out_db_data_preprocess = out_db_wo_join["py_conver_to_tensor"]
    out_db_data_compute = out_db_wo_join["py_compute"]

    # 1. 1st bar: out_db_wo_join
    ax.bar(index - bar_width - spacing, model_load_default, bar_width, color=colors[4], hatch=hatches[4], zorder=2,
           edgecolor='black')
    ax.bar(index - bar_width - spacing, out_db_data_query, bar_width, color=colors[0], hatch=hatches[0], zorder=2,
           bottom=model_load_default,
           edgecolor='black')
    ax.bar(index - bar_width - spacing, out_db_data_preprocess, bar_width, color=colors[2], hatch=hatches[2], zorder=2,
           bottom=model_load_default + out_db_data_query,
           edgecolor='black')
    ax.bar(index - bar_width - spacing, out_db_data_compute, bar_width, color=colors[3], hatch=hatches[3], zorder=2,
           bottom=model_load_default + out_db_data_query + out_db_data_preprocess,
           edgecolor='black')

    # 2. 2nd bar: out_db_join
    # in-db with optimizization
    # this is rust_python_switch_time + python_read_from_shared_memory_time
    in_db_data_copy_start_py = in_db_wo_join["mem_allocate_time"] + in_db_wo_join["python_compute_time"] - \
                               in_db_wo_join[
                                   "py_overall_duration"]
    in_db_data_query = in_db_wo_join["data_query_time"]
    in_db_data_preprocess = in_db_wo_join["py_conver_to_tensor"]
    in_db_data_compute = in_db_wo_join["py_compute"]

    ax.bar(index - bar_width / 2, model_load_default, bar_width, color=colors[4], hatch=hatches[4], zorder=2,
           edgecolor='black')

    ax.bar(index - bar_width / 2, model_load_default, bar_width, color=colors[4], hatch=hatches[4], zorder=2,
           label=label_in_db_model_load,
           edgecolor='black')

    ax.bar(index - bar_width / 2, in_db_data_query, bar_width, color=colors[0], hatch=hatches[0], zorder=2,
           label=label_in_db_data_query,
           bottom=model_load_default,
           edgecolor='black')
    ax.bar(index - bar_width / 2, in_db_data_copy_start_py, bar_width, color=colors[1], hatch=hatches[1],
           zorder=2,
           bottom=model_load_default + in_db_data_query,
           label=label_in_db_data_copy_start_py,
           edgecolor='black')
    ax.bar(index - bar_width / 2, in_db_data_preprocess, bar_width, color=colors[2],
           hatch=hatches[2], zorder=2,
           bottom=model_load_default + in_db_data_query + in_db_data_copy_start_py,
           label=label_in_db_data_preprocess, edgecolor='black')
    ax.bar(index - bar_width / 2, in_db_data_compute, bar_width, color=colors[3], hatch=hatches[3], zorder=2,
           bottom=model_load_default + in_db_data_query + in_db_data_copy_start_py + in_db_data_preprocess,
           label=label_in_db_data_compute, edgecolor='black')

    # 3. 3rd bar: in_db_wo_join
    out_db_data_query = out_db_join["data_query_time"]
    out_db_data_preprocess = out_db_join["py_conver_to_tensor"]
    out_db_data_compute = out_db_join["py_compute"]

    ax.bar(index + bar_width / 2, model_load_default, bar_width, color=colors[4], hatch=hatches[4], zorder=2,
           edgecolor='black')
    ax.bar(index + bar_width / 2, out_db_data_query, bar_width, color=colors[0], hatch=hatches[0], zorder=2,
           bottom=model_load_default,
           edgecolor='black')
    ax.bar(index + bar_width / 2, out_db_data_preprocess, bar_width, color=colors[2], hatch=hatches[2], zorder=2,
           bottom=model_load_default + out_db_data_query,
           edgecolor='black')
    ax.bar(index + bar_width / 2, out_db_data_compute, bar_width, color=colors[3], hatch=hatches[3], zorder=2,
           bottom=model_load_default + out_db_data_query + out_db_data_preprocess,
           edgecolor='black')

    # 4. 4th bar: in_db_join
    in_db_data_copy_start_py = in_db_join["mem_allocate_time"] + in_db_join["python_compute_time"] - \
                               in_db_join[
                                   "py_overall_duration"]
    in_db_data_query = in_db_join["data_query_time"]
    in_db_data_preprocess = in_db_join["py_conver_to_tensor"]
    in_db_data_compute = in_db_join["py_compute"]

    ax.bar(index + bar_width + spacing, model_load_default, bar_width, color=colors[4], hatch=hatches[4], zorder=2,
           label=label_in_db_model_load,
           edgecolor='black')
    ax.bar(index + bar_width + spacing, in_db_data_query, bar_width, color=colors[0], hatch=hatches[0], zorder=2,
           label=label_in_db_data_query,
           bottom=model_load_default,
           edgecolor='black')
    ax.bar(index + bar_width + spacing, in_db_data_copy_start_py, bar_width, color=colors[1], hatch=hatches[1],
           zorder=2,
           bottom=model_load_default + in_db_data_query,
           label=label_in_db_data_copy_start_py,
           edgecolor='black')
    ax.bar(index + bar_width + spacing, in_db_data_preprocess, bar_width, color=colors[2],
           hatch=hatches[2], zorder=2,
           bottom=model_load_default + in_db_data_query + in_db_data_copy_start_py,
           label=label_in_db_data_preprocess, edgecolor='black')
    ax.bar(index + bar_width + spacing, in_db_data_compute, bar_width, color=colors[3], hatch=hatches[3], zorder=2,
           bottom=model_load_default + in_db_data_query + in_db_data_copy_start_py + in_db_data_preprocess,
           label=label_in_db_data_compute, edgecolor='black')

    # Update the flags to ensure the labels are not set again in the next iterations
    set_label_in_db_data_query = False
    set_label_in_db_data_copy_start_py = False
    set_label_in_db_data_preprocess = False
    set_label_in_db_data_compute = False
    set_label_in_db_data_others = False
    set_label_in_db_model_load = False

    index += 1

# measure the speedups
for ele in speed_up_list:
    dataset = ele[0]
    in_db_t = ele[1]
    out_db_t = ele[2]
    print(f"{dataset}, Speedups = {out_db_t / in_db_t}")

# legned etc
ax.set_ylabel(".", fontsize=20, color='white')
fig.text(0.01, 0.5, 'Response Time (ms)', va='center', rotation='vertical', fontsize=20)

ax.set_ylim(top=4500)

ax.set_xticks(indices)
ax.set_xticklabels(datasets, rotation=0, fontsize=set_font_size)

# ax.legend(fontsize=set_lgend_size - 2, ncol=2, )
# ax.legend(fontsize=set_lgend_size, ncol=2, loc='upper left')

# Since the yaxis formatter is tricky with brokenaxes, you might need to set it for the actual underlying axes:
ax.yaxis.set_major_formatter(thousands_format)

ax.tick_params(axis='y', which='major', labelsize=set_font_size)

ax.grid(True, zorder=1)  # grid in front of bars

plt.tight_layout()
fig.tight_layout()
# plt.show()
print(f"saving to ./internal/ml/model_slicing/exp_imgs/macro_join.pdf")
fig.savefig(f"./internal/ml/model_slicing/exp_imgs/macro_join.pdf",
            bbox_inches='tight')
