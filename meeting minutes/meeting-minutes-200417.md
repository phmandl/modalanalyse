# Meeting minutes of 2020/04/17

## Team: The Coupled Oscillators

### Roles

- Philipp Mandl (chairman)
- Richard Schreiner (secretary)
- Maximilian Hoffmann
- Tae-Hyong Kim

### Main Discussion

1. The main reason for todays meeting was to finalize our solution to the homework.

2. Task 1 was explained by Richard to the other teammates. Again,Discords screensharing ability turned out to be very useful. Main insights were:
    - Choosing the right timebase for the time integration, i.e. the array evaluated by the integration function, is crucial for the correct computation of the system dynamics. If the timestep is too small, the computational effort becomes unfeasible. If it's too big, essential dynamics are not captured.
    - Animating the displacements in Jupyter can take some time unless one chooses the amount of frames for the callback function carefully. 

3. For the better part task 2 was already discussed over last time. A few minor changes were added. Mainly we examined the influence of different rayleigh damping constants on the response plots. 

4. As usual we agreed on the merging procedure in our repo and added some finishing touches.

### Main Difficulty

Apart from the joy of debugging minor errors, implementing the animations were the most challenging part. It turned out that JSAnimation is deprecated by now, however we were able to get by with the matplotlib.animation module just fine.

## Main Insight

The difference in computation time for some problems was remarkable. The usage of algorithms and data structures for sparse matrices was also a big difference - standard dense computation was almost intractable when we compared them side by side.