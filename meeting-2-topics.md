# Meeting minutes of 2020/03/18

## Team: The Coupled Oscillators
### Roles
  - Philipp Mandl (chairman)
  - Richard Schreiner (secretary)
  - Maximilian Hoffmann
  - Tae-Hyong Kim

## Main Discussion
1. Our team met online via our Discord server.
2. Then, we merged all our task branches in our GitHub repo. 
3. We distributed the programming tasks evenly in our last meeting. Today we explained our code to each other using the screencast function in Discord:
    - Vector iterators were written by Philipp and Max:
    The code was well documented and thus easily understood by all team mates. The Rayleigh-quotient variant turned out to be the fastest of the vector iteration methods. 
    - The QR algorithm was implemented by Richard:
    With the QR algorithm, all eigenvalues were computed effectively. However, it was not possible to find the eigenvectors using the updated Q matrices. The shifted vector iteration using the known eigenvalues however works fine. All methods were compared with the reference NumPy implementation.
    - Tae-Hyong took care of the eigenmode visualization, a few bugs and issues had to be corrected together.
4. Finally we concluded which final steps are necessary for submission of the first homework.

## Main Difficulty
The main difficulty was to organize and communicate everything remotely due to the special circumstances of the covid-19 situation.

## Main Insight
The QR algorithm proved to be effective to compute all the eigenvalues. The 
