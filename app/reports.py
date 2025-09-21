class Reports:

    def __generate_associations(self, objects, key, value): 
        association_dict = {}
        for object in objects:
            if object[key] not in association_dict:
                association_dict[object[key]] = list(object[value])
            else:
                x = association_dict[object[key]]
                x.append(object[value])
        return association_dict
                
    def student_performance(self, objects):

        def sort_by_grade(e):
            return e['grade']

        performance_dict = self.__generate_associations(objects, 'student_name', 'grade')
        performance_list = []
        for student in performance_dict.items():
            average = 0.0
            for grade in student[1]:
                average += float(grade)
            average = average / len(student[1])
            performance_list.append({
                'student_name' : student[0],
                'grade': average
                })
        performance_list.sort(key=sort_by_grade, reverse=True)
        return performance_list

