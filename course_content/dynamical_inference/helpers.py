"""Helper Functions

"""
import numpy as np
import jax.numpy as jnp
from jax.tree_util import tree_map
from torch.utils.data import Dataset
from torch.utils.data import DataLoader, default_collate

class CustomDataset(Dataset):
    """Custom Dataset. Holds datapoints of the form (t0, x0, t1, ts, xs)
    """
    
    def __init__(self, data):
        self.dataset = np.array(data, dtype=object)

    def __len__(self):
        return len(self.dataset)
    
    def __getitem__(self, idx):
        t0, x0, t1, ts, xs = self.dataset[idx]
        return t0, x0, t1, ts, xs


class NumpyLoader(DataLoader):
    """Custom DataLoader to return numpy arrays instead of torch tensors.
    """

    def __init__(self, dataset, batch_size=1,
                 shuffle=False, sampler=None,
                 batch_sampler=None, num_workers=0,
                 pin_memory=False, drop_last=False,
                 timeout=0, worker_init_fn=None):
        super(self.__class__, self).__init__(
            dataset,
            batch_size=batch_size,
            shuffle=shuffle,
            sampler=sampler,
            batch_sampler=batch_sampler,
            num_workers=num_workers,
            collate_fn=lambda b: tree_map(jnp.asarray, default_collate(b)),
            pin_memory=pin_memory,
            drop_last=drop_last,
            timeout=timeout,
            worker_init_fn=worker_init_fn
        )
