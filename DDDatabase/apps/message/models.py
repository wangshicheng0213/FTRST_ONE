# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
# 数据库表的增删改查

class UserMessage(models.Model):
    # verbose_name可以看作是对字段的注释
    object_id = models.CharField(max_length=50,verbose_name=u"主键")
    name = models.CharField(max_length=20, null=True, blank=True, default="", verbose_name=u"用户名")
    email = models.EmailField(verbose_name=u"邮箱")
    address = models.CharField(max_length=100, verbose_name=u"联系地址")
    message = models.CharField(max_length=500, verbose_name=u"留言信息")

    class Meta:
        # 数据库表的显示信息
        verbose_name = u"用户留言信息"
        verbose_name_plural = verbose_name

        # db_table ="user_message"
        # ordering ='-object_id'

class DDKBGene(models.Model):

    # verbose_name可以看作是对字段的注释
    # 主键不可以为空
    EnsemblId = models.CharField(null=True, blank=True, default="", max_length=100,verbose_name=u"Ensemble数据库中对基因的命名")
    Symbol = models.CharField(null=True, blank=True, default="", max_length=100,verbose_name=u"危险基因名称")
    EntrezId = models.CharField(max_length=100,verbose_name=u"基因的唯一标识符",primary_key = True)
    Chr = models.CharField(null=True,blank=True, default="", max_length=100, verbose_name=u"基因在染色体上的位置")
    Start = models.CharField(null=True, blank=True, default="", max_length=100,verbose_name=u"起始点")
    End = models.CharField(null=True, blank=True, default="", max_length=100,verbose_name=u"终止点")

    class Meta:
        # 数据库表的显示信息
        verbose_name = u"基因信息"
        verbose_name_plural = verbose_name

        # db_table ="DDKBGene"
        # ordering ='-object_id'


# class DDKBHumanPPI(models.Model):
#     # verbose_name可以看作是对字段的注释
#     # 主键不可以为空
#     Pubmed_ID = models.IntegerField(verbose_name=u"文献ID")
#
#     Synonyms_Interactor_A = models.IntegerField(null=True,blank=True,default="",verbose_name=u"同义词A")
#     Synonyms_Interactor_B = models.CharField(max_length=100,null=True,blank=True,default="",verbose_name=u"同义词B")
#
#     Organism_Interactor_A = models.IntegerField(verbose_name=u"NCBI分类IDA")
#     Organism_Interactor_B = models.IntegerField( verbose_name=u"NCBI分类IDB")
#
#     Author = models.CharField(max_length=100, verbose_name=u"作者")
#
#     BioGRID_Interaction_ID = models.IntegerField(verbose_name=u"交互的唯一标识符")
#
#     Throughput = models.IntegerField( verbose_name=u"吞吐量")
#
#     Systematic_Name_Interactor_A = models.CharField(max_length=100,null=True,blank=True,default="",verbose_name=u"纯文本系统名称A")
#     Systematic_Name_Interactor_B = models.CharField(max_length=100,null=True,blank=True,default="",verbose_name=u"纯文本系统名称B")
#
#     Qualifications = models.CharField(max_length=100,null=True,blank=True,default="",verbose_name=u"限定符")
#
#     Modification = models.CharField(max_length=100,null=True,blank=True,default="",verbose_name=u"修饰修改")
#
#     Score = models.IntegerField(default="", verbose_name=u"分数")
#
#     Source_Database = models.CharField(max_length=100, verbose_name=u"源数据库")
#
#     Official_Symbol_Interactor_A = models.CharField(max_length=100, verbose_name=u"交互器A的官方名称")
#     Official_Symbol_Interactor_B = models.CharField(max_length=100, verbose_name=u"交互器B的官方名称")
#
#     BioGRID_ID_Interactor_A = models.IntegerField(verbose_name=u"交互A的ID")
#     BioGRID_ID_Interactor_B = models.IntegerField(verbose_name=u"交互B的ID")
#
#     Entrez_Gene_Interactor_A = models.IntegerField(verbose_name=u"交互基因的EntrezGeneA")
#     Entrez_Gene_Interactor_B = models.IntegerField(verbose_name=u"交互基因的EntrezGeneB")
#
#     Phenotypes = models.CharField(max_length=100,null=True,blank=True,default="",verbose_name=u"表型")
#
#
#     Experimental_System = models.CharField(max_length=100, verbose_name=u"实验系统名称")
#     Experimental_System_Type = models.CharField(max_length=100, verbose_name=u"实验系统类型")
#
#     Tags = models.CharField(max_length=100,null=True,blank=True,default="", verbose_name=u"标签")
#
#
#     class Meta:
#         # 数据库表的显示信息
#         verbose_name = u"人类蛋白质相互作用信息"
#         verbose_name_plural = verbose_name
#
#         # db_table ="DDKBHumanPPI"
#         # ordering ='-object_id'
#
# class DDKBCoexpressionSpace(models.Model):
#     # verbose_name可以看作是对字段的注释
#     # 主键不可以为空
#     Ages = models.CharField(max_length= 100, verbose_name=u"不同的年龄段")
#     Related_gene = models.CharField(max_length=100, null=True,blank=True,default="",verbose_name=u"关联基因")
#     Co_expression_gene = models.CharField(max_length=100,verbose_name=u"共表达基因")
#     Pearson = models.IntegerField(verbose_name=u"皮尔逊的相关系数")
#     P_value = models.IntegerField(verbose_name=u"共表达中的显著性的大小")
#
#
#     class Meta:
#         # 数据库表的显示信息
#         verbose_name = u"同一时间不同脑区的表达"
#         verbose_name_plural = verbose_name
#
#         # db_table ="DDKBCoexpressionSpace"
#         # ordering ='-object_id'
#
#
# class DDKBCoexpressionTime(models.Model):
#     # verbose_name可以看作是对字段的注释
#     # 主键不可以为空
#     Structureid = models.IntegerField(verbose_name=u"不同的脑区")
#     Relatedgene = models.CharField(max_length=100, null=True,blank=True,default="",verbose_name=u"关联基因")
#     Coexpressiongene = models.CharField(max_length=100, verbose_name=u"共表达基因")
#     Pearson = models.IntegerField(verbose_name=u"皮尔逊的相关系数")
#     Pvalue = models.IntegerField(verbose_name=u"共表达中的显著性的大小")
#
#     class Meta:
#         # 数据库表的显示信息
#         verbose_name = u"同意脑区不同时间表达"
#         verbose_name_plural = verbose_name
#
#         # db_table ="DDKBCoexpressionTime"
#         # ordering ='-object_id'
#
# class DDKBPPISample(models.Model):
#     # verbose_name可以看作是对字段的注释
#     # 主键不可以为空
#
#     OfficialSymbolInteractorA = models.CharField(max_length=100, null=True,blank=True,default="",verbose_name=u"关联基因A")
#     OfficialSymbolInteractorB = models.CharField(max_length=100, null=True, blank=True, default="", verbose_name=u"关联基因B")
#
#     class Meta:
#         # 数据库表的显示信息
#         verbose_name = u"同意脑区不同时间表达"
#         verbose_name_plural = verbose_name
#
#         # db_table ="DDKBCoexpressionTime"
#         # ordering ='-object_id'


class Post(models.Model):
    # 标题
    title = models.CharField(max_length=70)
    # 正文
    body = models.TextField()


    # 其他属性
    def __str__(self):
        return self.title