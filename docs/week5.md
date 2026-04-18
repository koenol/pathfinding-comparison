# W5 Progress Report

- Last week review by the course staff it was noted that JPS avg performance is too slow, meaning either test data or the pathfinder itself has a performance issue. First I tried to exclude runs that had a very high running times, but the avg runtime did not seem to go down much, after which I created a temporary decorator to keep track of individual methods runtime. Based on the observation It seems jps_jump method has the highest runtime so further examination is required.
- New tests have been added, will need to focus more on JPS classes tests after I managed to fix the speed issue.
- Fixed majority of pylint issues, remaining require refactoring.
- Peer review done

Total Hours: 4h