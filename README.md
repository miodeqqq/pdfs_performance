Python-PDF libraries performance tests
======================================

Checking performance with reading PDF and:
- **gathering info about the number of pages using python libraries.**
- **... some day ...**

**Current stable version:** v1.0

**Release date:** 07.08.2019

### Author:
Maciej Januszewski (maciek@mjanuszewski.pl)

### Pre-requirements:

* **Firstly run Apache-Tika Server (for Tika purposes):** 
```
docker pull logicalspark/docker-tikaserver
docker run -d -p 9998:9998 logicalspark/docker-tikaserver
```

### Running as human:
```
./run.py <path/to/pdfs_data/>
```


### Sample plots outputs:
**- Final statistics - overall processing time:**
![Scatter plot generated by plotly](./sample_data/final_libs_stats.png)

**- Final statistisc - bar chart:**
![Boxes plot generated by plotly](./sample_data/final_libs_comparison.png)
