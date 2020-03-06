a = 5.0;
b = 3.0;
h = 0.02;
Nx = 19; // for a
Ny = 11; // for b
Nz = 2;
Point(1) = {a/2, b/2, 0, 1.0};
Point(2) = {-a/2, b/2, 0, 1.0};
Point(3) = {-a/2, -b/2, 0, 1.0};
Point(4) = {a/2, -b/2, 0, 1.0};
Line(1) = {4, 1};
Line(2) = {1, 2};
Line(3) = {2, 3};
Line(4) = {3, 4};
Line Loop(5) = {1, 2, 3, 4};
Plane Surface(6) = {5};

Transfinite Line{4,2} = Nx + 1;
Transfinite Line{1,3} = Ny + 1;
Transfinite Surface{6};
Recombine Surface{6};

up[] = Extrude {0, 0, h/2} {
  Surface{6};
  Layers{Nz}; 
  Recombine;
};
do[] = Extrude {0, 0, -h/2} {
  Surface{6};
  Layers{Nz}; 
  Recombine;
};
Physical Line('L_edge') = {1,2,3,4};
Physical Surface('S_mid') = {6};
Physical Volume('V_plate') = { up[1],do[1] };
