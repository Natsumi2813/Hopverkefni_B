
#import <Foundation/Foundation.h>

@interface myClass : NSObject 


@end

@implementation myClass

-(void)Print
{
    NSLog(@"Halló Daniel!");
}

@end


int main(int argc, const char * argv[]) {
    @autoreleasepool {
        myClass *c = [myClass init];
        [c Print];
    }
    return 0;
}
