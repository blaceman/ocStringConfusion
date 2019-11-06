//
//  TTStrUnConfusion.m
//  teststring
//
//  Created by blaceman on 2019/10/29.
//  Copyright © 2019 new4545. All rights reserved.
//

#import "TTStrUnConfusion.h"

@implementation TTStrUnConfusion


+ (NSString *)getOtherStr:(NSString *)str{
    NSString *temp = @"";
    for(int i =0; i < [str length]; i++){
        if (i % 2) {
            NSString *someStr = [str substringWithRange:NSMakeRange(i, 1)];
            if ([someStr isEqualToString:@"*"]) {
                someStr = @"\\";
            }
            temp = [NSString stringWithFormat:@"%@%@",temp,someStr];
        }
    }
    if ([temp containsString:@"\\n"]) {
        temp = [temp stringByReplacingOccurrencesOfString:@"\\n" withString:@"\n"];
    }
    if ([temp containsString:@"\\t"]) {
        temp = [temp stringByReplacingOccurrencesOfString:@"\\t" withString:@"\t"];
    }
    return temp;
}

@end
