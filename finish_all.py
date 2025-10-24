def build_dependency(total_jobs, dependents):
    dependent_dict = {}

    for a, b in dependents:
        dependent_dict.setdefault(a, set()).add(b)

    all_jobs = set(range(total_jobs))
    finished_jobs = all_jobs - set(dependent_dict.keys())

    return dependent_dict, finished_jobs


def finish_all(total_jobs, dependents):
    dependent_dict, finished_jobs = build_dependency(total_jobs, dependents)

    if not finished_jobs:
        return False
    if not dependent_dict:
        return True

    circuit = True
    while len(finished_jobs) < total_jobs and circuit:
        circuit = False
        for job, prereqs in dependent_dict.items():
            if job not in finished_jobs and all(p in finished_jobs for p in prereqs):
                finished_jobs.add(job)
                circuit = True
                if len(finished_jobs) == total_jobs:
                    return True
    return False


if __name__ == "__main__":
    job_list = [
        (2, [(1, 0)]),
        (2, [(1, 0), (0, 1)]),
        (3, [(1, 0), (2, 1)]),
        (1, []),
        (11, [(6, 10), (4, 3), (9, 2), (2, 3), (6, 1), (2, 8), (10, 1), (10, 2), (5, 3), (0, 10), (7, 4), (6, 1)]),
    ]
    for total_jobs, dependents in job_list:
        output = finish_all(total_jobs, dependents)
        print(f"output = {output}")
