Ax, Ay, Bx, By, Cx, Cy = map(int,input().split())

print(abs(((Ax-Cx)*(By-Cy)-(Bx-Cx)*(Ay-Cy))/2))