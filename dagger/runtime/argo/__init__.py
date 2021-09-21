"""
Compile DAGs into manifests that will run on top of [Argo Workflows](https://argoproj.github.io/projects/argo).

This runtime produces Python mappings (dictionaries) that contain all the necessary Kubernetes resources for Argo Workflows to execute the supplied DAG.

Please note that this runtime doesn't produce JSON/YAML files. Users will still need to take the manifests generated by this runtime and apply them to a Kubernetes cluster.

This runtime requires a container image and entrypoint to be specified, and assumes the supplied entrypoint exposes the same DAG that was used to generate the manifests through the CLI runtime.

Please check the Argo runtime user guide for more details.
"""

from dagger.runtime.argo.cron import Cron, CronConcurrencyPolicy  # noqa
from dagger.runtime.argo.metadata import Metadata  # noqa
from dagger.runtime.argo.v1alpha1 import (  # noqa
    cluster_workflow_template_manifest,
    cron_workflow_manifest,
    workflow_manifest,
    workflow_template_manifest,
)
from dagger.runtime.argo.workflow import Workflow  # noqa
