
import matplotlib.pyplot as plt

def draw_gantt_chart(processes):

    if not processes:
        return

    # Get process IDs (excluding context switches)
    pids = list(dict.fromkeys(
        p["pid"] for p in processes
        if p["pid"] not in ("cs", "half_cs")
    ))

    fig, ax = plt.subplots(figsize=(12, 5))

    colors = plt.cm.tab10.colors
    color_map = {
        pid: colors[i % len(colors)]
        for i, pid in enumerate(pids)
    }

    # Draw execution intervals
    for p in processes:

        pid = p["pid"]

        # Skip context switches
        if pid in ("cs", "half_cs"):
            continue

        start = p["start_time"]
        end = p["end_time"]

        y = pids.index(pid)

        ax.barh(
            y,
            end - start,
            left=start,
            height=0.5,
            color=color_map[pid],
            edgecolor="black"
        )

        ax.text(
            (start + end) / 2,
            y,
            pid,
            ha="center",
            va="center",
            color="white",
            fontsize=10
        )

    # Configure axes
    ax.set_yticks(range(len(pids)))
    ax.set_yticklabels(pids)

    ax.set_xlabel("Time")
    ax.set_ylabel("Processes")
    ax.set_title("CPU Scheduling Gantt Chart")

    # Time boundaries
    times = sorted(set(
        [p["start_time"] for p in processes] +
        [p["end_time"] for p in processes]
    ))

    ax.set_xticks(times)

    ax.grid(axis="x", linestyle="--", alpha=0.5)
    ax.set_axisbelow(True)

    ax.invert_yaxis()
    plt.tight_layout()
    plt.show()
