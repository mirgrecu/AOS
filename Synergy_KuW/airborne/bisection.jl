# write a function that finds the closest element in a sorted array using bisection in julia
# input: x: sorted array, n: length of x, xval: value to find
function bisection(x,n,xval)
    istart=1
    iend=n
    while iend-istart>1
        imid=round(Int,(istart+iend)/2)
        if x[imid]>xval
            iend=imid
        else
            istart=imid
        end
    end
    return istart
end

