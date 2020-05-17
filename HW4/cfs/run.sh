#!/bin/sh

gmsh=/opt/programs/gmsh/gmsh-2.11.0-Linux/bin/gmsh
cfs=/opt/cfs/trunk_std/bin/cfs

$gmsh plate.geo -3
$cfs -p Plate3D.xml JOB
