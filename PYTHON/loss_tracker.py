#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

A simple class to track the loss of a model during training.
Oftentimes, your loss function is composed of multiple components, e.g.
for a VAE, you might have a reconstruction loss and a KL divergence loss.
You can use this class to track the individual components of the loss:

from loss_tracker import LossTracker

loss_tracker = LossTracker()

# During training, you can add losses like this:
loss_tracker.add_loss({'reconstruction_loss': 0.3, 'kl_divergence': 0.157})

# To get the average loss:
print(loss_tracker.report_loss())  # Output: reconstruction_loss: 0.3000 | kl_divergence: 0.1570

# At the end of an epoch, you can clear the tracker and get the average losses:
avg_losses = loss_tracker.clear()


File        :    loss_tracker.py
Author      :    Akira Nair
Contact     :    akira.nair@pennmedicine.upenn.edu

"""


class LossTracker:
    """
    Class to track the loss during training.
    """
    def __init__(self):
        self.losses = {}
        self.history = []

    def add_loss(self, losses: dict):
        """
        Add a dictionary of losses to the tracker.
        
        Args:
            losses (dict): Dictionary containing loss values.
        """
        if isinstance(losses, dict):
            for key, value in losses.items():
                if key not in self.losses:
                    self.losses[key] = [value]
                else:
                    self.losses[key].append(value)

    def report_loss(self):
        """
        Get the average loss from the tracked losses.
        
        Returns:
            float: The average loss.
        """
        out = {}
        for key in self.losses:
            out[key] = sum(self.losses[key]) / len(self.losses[key])
        
        # format as string
        out_str = ' | '.join([f"{k}: {v:.4f}" for k, v in out.items()])
        return out_str
    
    def clear(self):
        """
        Reset the tracked losses.
        """
        avg_losses = {k: sum(v) / len(v) for k, v in self.losses.items()}
        self.history.append(avg_losses)
        self.losses = {}
        return avg_losses
    
    def save_loss_history(self, path):
        """
        Save the loss history to a file.
        
        Args:
            path (str): Path to save the loss history.
        """
        import pandas as pd
        df = pd.DataFrame(self.history)
        df.to_csv(path, index=False)