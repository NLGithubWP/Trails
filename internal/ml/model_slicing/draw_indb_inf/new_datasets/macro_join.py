import json
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np
from matplotlib.ticker import FuncFormatter
from brokenaxes import brokenaxes


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
        'in_db_join': {'model_init_time': 0.009772562, 'data_type_convert_time': 1.186813152,
                       'data_query_time': 2.589222349, 'python_compute_time': 0.449734902,
                       'overall_query_latency': 3.078992093, 'diff': -0.030262280000000086,
                       'mem_allocate_time': 0.030250188, 'data_query_time_spi': 1.3818609099999999,
                       'py_conver_to_tensor': 0.014644145965576172, 'py_compute': 0.38569045066833496,
                       'py_overall_duration': 0.40750551223754883, 'py_diff': 0.007170915603637695},

        'in_db_wo_join': {'mem_allocate_time': 0.046573999, 'data_query_time_spi': 0.343235082,
                          'python_compute_time': 0.501055263, 'model_init_time': 0.009541483,
                          'overall_query_latency': 2.195732048, 'diff': -0.046581859999999864,
                          'data_type_convert_time': 1.247244199, 'data_query_time': 1.638553442,
                          'py_conver_to_tensor': 0.014708757400512695, 'py_compute': 0.39806079864501953,
                          'py_overall_duration': 0.42017054557800293, 'py_diff': 0.007400989532470703}
        ,
    },

    # Diabetes dataset
    'Diabetes': {
        'in_db_join': {'diff': -0.02079015999999978, 'model_init_time': 0.009885554,
                       'data_type_convert_time': 0.83870191, 'data_query_time': 2.320049377,
                       'mem_allocate_time': 0.020779264, 'python_compute_time': 0.512643846,
                       'overall_query_latency': 2.8633689369999997, 'data_query_time_spi': 1.452491238,
                       'py_conver_to_tensor': 0.01607990264892578, 'py_compute': 0.4545469284057617,
                       'py_overall_duration': 0.4778456687927246, 'py_diff': 0.007218837738037109}
        ,
        'in_db_wo_join': {'mem_allocate_time': 0.027362219, 'model_init_time': 0.010055741,
                          'data_query_time_spi': 0.166548796, 'data_query_time': 1.029582073,
                          'python_compute_time': 0.487216135, 'overall_query_latency': 1.554225487,
                          'data_type_convert_time': 0.841480709, 'diff': -0.02737153800000014,
                          'py_conver_to_tensor': 0.01747870445251465, 'py_compute': 0.42203354835510254,
                          'py_overall_duration': 0.45314645767211914, 'py_diff': 0.013634204864501953}
        ,
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

    indb_med_opt = scale_to_ms(valuedic["in_db_join"])
    outcpudb_med = scale_to_ms(valuedic["in_db_wo_join"])

    speed_up_list.append([dataset, indb_med_opt["overall_query_latency"], outcpudb_med["overall_query_latency"]])

    # set labesl
    label_in_db_model_load = 'Model Loading' if set_label_in_db_model_load else None
    label_in_db_data_query = 'Data Retrieval' if set_label_in_db_data_query else None
    label_in_db_data_copy_start_py = 'Data Copying' if set_label_in_db_data_copy_start_py else None
    label_in_db_data_preprocess = 'Data Preprocessing' if set_label_in_db_data_preprocess else None
    label_in_db_data_compute = 'Inference' if set_label_in_db_data_compute else None
    label_in_db_data_others = 'Others' if set_label_in_db_data_others else None

    # in-db with optimizization
    in_db_data_model_load = indb_med_opt["model_init_time"]
    # this is rust_python_switch_time + python_read_from_shared_memory_time
    in_db_data_copy_start_py = indb_med_opt["mem_allocate_time"] + indb_med_opt["python_compute_time"] - indb_med_opt[
        "py_overall_duration"]
    in_db_data_query = indb_med_opt["data_query_time"]
    in_db_data_preprocess = indb_med_opt["py_conver_to_tensor"]
    in_db_data_compute = indb_med_opt["py_compute"]

    ax.bar(index + bar_width + spacing, in_db_data_model_load, bar_width, color=colors[4], hatch=hatches[4], zorder=2,
           label=label_in_db_model_load,
           edgecolor='black')
    ax.bar(index + bar_width + spacing, in_db_data_query, bar_width, color=colors[0], hatch=hatches[0], zorder=2,
           label=label_in_db_data_query,
           bottom=in_db_data_model_load,
           edgecolor='black')
    ax.bar(index + bar_width + spacing, in_db_data_copy_start_py, bar_width, color=colors[1], hatch=hatches[1],
           zorder=2,
           bottom=in_db_data_model_load + in_db_data_query,
           label=label_in_db_data_copy_start_py,
           edgecolor='black')
    ax.bar(index + bar_width + spacing, in_db_data_preprocess, bar_width, color=colors[2],
           hatch=hatches[2], zorder=2,
           bottom=in_db_data_model_load + in_db_data_query + in_db_data_copy_start_py,
           label=label_in_db_data_preprocess, edgecolor='black')
    ax.bar(index + bar_width + spacing, in_db_data_compute, bar_width, color=colors[3], hatch=hatches[3], zorder=2,
           bottom=in_db_data_model_load + in_db_data_query + in_db_data_copy_start_py + in_db_data_preprocess,
           label=label_in_db_data_compute, edgecolor='black')

    ax.bar(index + bar_width / 2, in_db_data_model_load, bar_width, color=colors[4], hatch=hatches[4], zorder=2,
           edgecolor='black')
    ax.bar(index + bar_width / 2, in_db_data_query, bar_width, color=colors[0], hatch=hatches[0], zorder=2,
           bottom=in_db_data_model_load,
           edgecolor='black')
    ax.bar(index + bar_width / 2, in_db_data_copy_start_py, bar_width, color=colors[2], hatch=hatches[2], zorder=2,
           bottom=in_db_data_model_load + in_db_data_query,
           edgecolor='black')
    ax.bar(index + bar_width / 2, in_db_data_compute, bar_width, color=colors[3], hatch=hatches[3], zorder=2,
           bottom=in_db_data_model_load + in_db_data_query + in_db_data_copy_start_py + in_db_data_preprocess,
           edgecolor='black')

    # # out-db CPU
    out_db_data_query = outcpudb_med["data_query_time"]
    out_db_data_preprocess = outcpudb_med["py_conver_to_tensor"]
    out_db_data_compute = outcpudb_med["py_compute"]

    ax.bar(index - bar_width / 2, in_db_data_model_load, bar_width, color=colors[4], hatch=hatches[4], zorder=2,
           edgecolor='black')
    ax.bar(index - bar_width / 2, out_db_data_query, bar_width, color=colors[0], hatch=hatches[0], zorder=2,
           bottom=in_db_data_model_load,
           edgecolor='black')
    ax.bar(index - bar_width / 2, out_db_data_preprocess, bar_width, color=colors[2], hatch=hatches[2], zorder=2,
           bottom=in_db_data_model_load + out_db_data_query,
           edgecolor='black')
    ax.bar(index - bar_width / 2, out_db_data_compute, bar_width, color=colors[3], hatch=hatches[3], zorder=2,
           bottom=in_db_data_model_load + out_db_data_query + out_db_data_preprocess,
           edgecolor='black')

    ax.bar(index - bar_width - spacing, in_db_data_model_load, bar_width, color=colors[4], hatch=hatches[4], zorder=2,
           edgecolor='black')
    ax.bar(index - bar_width - spacing, out_db_data_query, bar_width, color=colors[0], hatch=hatches[0], zorder=2,
           bottom=in_db_data_model_load,
           edgecolor='black')
    ax.bar(index - bar_width - spacing, out_db_data_preprocess, bar_width, color=colors[2], hatch=hatches[2], zorder=2,
           bottom=in_db_data_model_load + out_db_data_query,
           edgecolor='black')
    ax.bar(index - bar_width - spacing, out_db_data_compute, bar_width, color=colors[3], hatch=hatches[3], zorder=2,
           bottom=in_db_data_model_load + out_db_data_query + out_db_data_preprocess,
           edgecolor='black')

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

# ax.set_ylim(top=2200)

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
