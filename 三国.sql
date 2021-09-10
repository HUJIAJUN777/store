SELECT ename,deptno FROM `t_employees` WHERE deptno=30;
SELECT empno,ename,deptno FROM `t_employees` WHERE job='经理';
SELECT ename,sal,comm FROM `t_employees` WHERE comm>sal;
SELECT ename,sal,comm FROM `t_employees` WHERE comm*0.6>sal;
SELECT ename,deptno,job FROM `t_employees` WHERE (job='经理' AND deptno=10)OR(job='分析员' AND deptno=20);
SELECT * FROM `t_employees` WHERE(job='经理' AND deptno=10)OR(job='分析员' AND deptno=20)OR(sal>=3000 AND job!='武装上将' AND job!='经理');
SELECT * FROM`t_employees` WHERE comm<1000 OR comm IS NULL;
SELECT * FROM`t_employees` WHERE ename LIKE'___';
SELECT * FROM`t_employees` WHERE hiredate>='2000-01-01';
SELECT * FROM`t_employees`  ORDER BY empno;
SELECT * FROM`t_employees` ORDER BY sal DESC,hiredate ASC;
SELECT deptno,AVG(sal)'平均工资'FROM`t_employees` GROUP BY deptno;
SELECT deptno,COUNT(*)'员工数量'FROM `t_employees` GROUP BY deptno;
SELECT job,MAX(sal)'最高工资',MIN(sal)'最低工资',COUNT(*)'人数'FROM`t_employees`GROUP BY job;


