% calculates rho* = 0.8 so as to compare to rho* = 0.868
f1=fopen('data.short');
%%%% Parameters to vary %%%%
Nmax = 4000;
TimeStepSize = 0.005;
DumpInterval = 500;
%%%%%%%%%%%%%%%%%%%%%%%%%%
m = 0;
while ~ feof(f1)
    m = m + 1;
    NumberAtom=cell2mat(textscan(f1,'%f','headerLines',3));
    if NumberAtom>0
        C =cell2mat(textscan(f1,'%f%f%f%f%f','headerLines',5));
        B = sortrows (C,1);  % sort each timezone into ascending order ID
        [nr,nc] = size(B);
        DPT (:,:,m) = B (:,3:5);  % save every interval of data into DPT multi-array
    else
        break
    end
end
save ('RAW_Data_long', 'DPT');
fclose(f1);

%Tmax = m; %original
Tmax = m-1;
% Calculate MSD after D is loaded from dump file
% system specifics
TauMax = Tmax - 1;
fid = fopen('medium','w');
for i = 1 : TauMax
    for j = 1 : Nmax
        summation = 0;
        counter = 0;
        for k = 1 : Tmax - i
            counter = counter + 1;
            dist = (DPT (j,1,k) - DPT(j,1,k + i))^2 + (DPT (j,2,k) - DPT(j,2,k + i))^2 + (DPT (j,3,k) - DPT(j,3,k + i))^2;
            summation = summation + dist;
        end
            AveSummation = summation/counter;
           a(j,1) = AveSummation; 
    end
   TotSummation = sum(a);
   AveTotSummation = TotSummation/Nmax;
   tau = i * TimeStepSize * DumpInterval;
   fprintf(fid,'%d %4.4f %9.6f %d\n',i,tau,AveTotSummation,counter)
end
fclose(fid)
