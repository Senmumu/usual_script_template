# coding:utf-8
"""connect neo4j"""
from py2neo import Graph, Node, Relationship
import settings
from pandas import DataFrame


class NeoConn(object):
    """Connect neo4j"""

    def __init__(self):
        self._graph = Graph(host=settings.NEO4J_HOST, http_port=settings.NEO4J_PORT,
                            user=settings.NEO4J_USERNAME, password=settings.NEO4J_PASSWORD)

    def read_data(self, cql, *data_list):
        """读取数据"""
        return self._graph.data(cql, data_list)

    def read_df_data(self, cql, *data_list):
        """读取dataframe"""
        df = DataFrame(self._graph.data(cql, data_list))
        return df

    # def insert_data(self, * data_list):
    #     """输入数据"""
    #     tx = self._graph.begin()
    #     for col in data_list:
    #         for row in col:
    #             # print(row)
    #             a = Node("Disease", name=row['name_en'], name_cn=row['name_cn'],
    #                      bmj_id=row["bmj_id"], icd10_k_id=row['icd10_k_id'], category_cn=row['category_cn'], source="bmj_en")
    #             tx.create(a)
    #     tx.commit()
        # self._graph.schema.create_uniqueness_constraint()
        # self._graph.schema.create_index()
    # def insert_node(self, * data_list):
    #     """输入数据"""
    #     tx = self._graph.begin()
    #     for col in data_list:
    #         for row in col:
    #             # print(row)
    #             a = Node("DiagFactor", name=row['factor_name'].strip())
    #             tx.create(a)
    #     tx.commit()

    # def insert_relation(self, * data_list):
    #     """输入数据"""
    #     tx = self._graph.begin()
    #     for col in data_list:
    #         for row in col:
    #             # print(row)
    #             try:
    #                 a = self._graph.find_one(
    #                     "Disease", property_key="bmj_id", property_value=row["bmj_id"])
    #                 b = self._graph.find_one(
    #                     "DiagFactor", property_key='name', property_value=row['factor_name'].strip())
    #                 ab = Relationship(a, "HasDiagFactor", b,
    #                                   factor_class=row['factor_class'].strip(), factor_freq=row['factor_freq'].strip())
    #                 tx.create(ab)
    #             except Exception as identifier:
    #                 pass

    #     tx.commit()
        # tx = self._graph.begin()
        # for col in data_list:
        #     for row in col:
        #         # print(row)
        #         try:
        #             a = self._graph.find_one(
        #                 "Disease", property_key="bmj_id", property_value=row["bmj_id"])
        #             b = self._graph.find_one(
        #                 "RiskFactor", property_key='name', property_value=row['factor_name'].strip())
        #             ab = Relationship(a, "HasRiskFactor", b,
        #                               degree=row['degree'].strip())
        #             tx.create(ab)
        #         except Exception as identifier:
        #             pass

        # tx.commit()
