## Visualization planning

### Work done to date (12-18-17)

- nteract/packages/transform.dataresource/src
    - if MIME type
- table view


### Moving forward: specialized library that overrides show() and do cool stuff

#### Plot view (v1)
- Call show() receive a blob of data
- aggregation representation * on/off
- clearly communicate if sampled data displayed or not

#### Improved plot view (v-next)

- Call show() receive a blob of data
- aggregation representation * on/off
- clearly communicate if sampled data displayed or not
- progressive sampling to display better plot

#### paging view (v-next + 1)

- explains a warning when sample used
- sample and first x rows
- default: sampled
- Not sampled: does not support paging
- explore graph by swiping through data

### Concepts

#### proper sampling

- evaluate each partition
- random shuffle??
- tools that don't require a shuffle

#### persistence in the notebook

- notebook stores the json of the sample data
- point in time plot when sharing a notebook with others

#### show()

- spark 2.3 simple sample return pandas DataFrame
- support for callbacks later? If so, what needs to be done

#### UI

- franchise sidebar as inspiration
- rendering whatever at top level
- composite component (table, plot)
